import json
import random
import time
from datetime import datetime
import pika

def generate_download_event():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "coordinates": {
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180)
        },
        "file_size": random.randint(1000000, 100000000),
        "download_speed": random.uniform(0.1, 10.0)
    }

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
            
            while True:
                event = generate_download_event()
                channel.basic_publish(
                    exchange='',
                    routing_key='arrivals',
                    body=json.dumps(event)
                )
                print(f"Sent event")
                time.sleep(2)
        except pika.exceptions.AMQPConnectionError:
            print("Connection failed, retrying...")
            time.sleep(5)

if __name__ == "__main__":
    main()