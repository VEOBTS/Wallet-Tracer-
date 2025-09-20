# src/utils.py
from datetime import datetime
from decimal import Decimal

def ts_to_iso(ts):
    return datetime.utcfromtimestamp(int(ts)).isoformat() + "Z"

def to_decimal(value_wei, decimals=18):
    # value_wei: string or int
    return Decimal(value_wei) / (Decimal(10) ** decimals)
