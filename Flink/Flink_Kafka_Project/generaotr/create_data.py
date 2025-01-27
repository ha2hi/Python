import random
import datetime
import pytz
import uuid

def _get_id() -> str:
    return str(uuid.uuid4())

def _get_time_data() -> int:
    now = datetime.datetime.now()

    timestamp_ms = int(now.timestamp() * 1000)

    return timestamp_ms

def _get_trax_type() -> str:
    return random.choice(['CASH', 'CARD', 'BITCOIN'])

def _get_amount() -> int:
    return random.randint(0,100)

def generate_transaction_data() -> dict:
    return {
        'ID' : _get_id(),
        'TRANSACTION_TYPE' : _get_trax_type(),
        'AMOUNT' : _get_amount(),
        'DATE_MS' : _get_time_data(),
        'CURRENCY' : 'USD'
    }