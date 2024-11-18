import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from consumer import SCHEMA
from jsonschema import validate, ValidationError
import pytest

def test_valid_message():
    valid_msg = {
        "timestamp": "2024-01-01T12:00:00",
        "coordinates": {"latitude": 45.0, "longitude": -75.0},
        "file_size": 1000000,
        "download_speed": 5.0
    }
    validate(instance=valid_msg, schema=SCHEMA)


def test_invalid_coordinates():
    invalid_msg = {
        "timestamp": "2024-01-01T12:00:00",
        "coordinates": {"latitude": 91.0, "longitude": -75.0},
        "file_size": 1000000,
        "download_speed": 5.0
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_msg, schema=SCHEMA)

def test_missing_field():
    invalid_msg = {
        "timestamp": "2024-01-01T12:00:00",
        "coordinates": {"latitude": 45.0, "longitude": -75.0},
        "file_size": 1000000
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_msg, schema=SCHEMA)