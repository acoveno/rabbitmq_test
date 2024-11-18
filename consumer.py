import json
import pika
import time
from jsonschema import validate

SCHEMA = {
    "type": "object",
    "properties": {
        "timestamp": {"type": "string", "format": "date-time"},
        "coordinates": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number", "minimum": -90, "maximum": 90},
                "longitude": {"type": "number", "minimum": -180, "maximum": 180}
            },
            "required": ["latitude", "longitude"]
        },
        "file_size": {"type": "number", "minimum": 0},
        "download_speed": {"type": "number", "minimum": 0}
    },
    "required": ["timestamp", "coordinates", "file_size", "download_speed"]
}

def callback(ch, method, properties, body):
    try:
        event = json.loads(body)
        try:
            validate(instance=event, schema=SCHEMA)
            print("Valid event received:")
            print(json.dumps(event, indent=2))
            print("-" * 50)
        except Exception:
            print("Invalid event, redirecting to rejects")
            ch.basic_publish(
                exchange='',
                routing_key='rejects',
                body=body
            )
    except json.JSONDecodeError:
        print("Invalid JSON received, redirecting to rejects")
        ch.basic_publish(
            exchange='',
            routing_key='rejects',
            body=body
        )

def main():
    while True:
        try:
            credentials = pika.PlainCredentials('admin', 'admin')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters('rabbitmq', 5672, 'test', credentials)
            )
            channel = connection.channel()
            
            channel.queue_declare(queue='arrivals')
            channel.queue_declare(queue='rejects')
            
            channel.basic_consume(
                queue='arrivals',
                on_message_callback=callback,
                auto_ack=True
            )
            
            print("Waiting for messages on arrivals queue. To exit press CTRL+C")
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError:
            print("Connection failed, retrying...")
            time.sleep(5)

if __name__ == "__main__":
    main()