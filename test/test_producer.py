import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from producer import generate_download_event
from datetime import datetime

#Can add more based on biz logic

def test_generate_download_event():
    event = generate_download_event()
    assert isinstance(event, dict)
    assert "timestamp" in event
    assert "coordinates" in event
    assert "file_size" in event
    assert "download_speed" in event
    
    # Test coordinate bounds
    assert -90 <= event["coordinates"]["latitude"] <= 90
    assert -180 <= event["coordinates"]["longitude"] <= 180
    
    # Test positive values
    assert event["file_size"] > 0
    assert event["download_speed"] > 0
    
    # Test timestamp format
    datetime.fromisoformat(event["timestamp"])