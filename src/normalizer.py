# src/normalizer.py
from .utils import ts_to_iso, to_decimal
from decimal import Decimal
from typing import List, Dict

def normalize_normal_tx(tx: Dict) -> Dict:
    """
    Convert Etherscan normal tx to normalized row
    """
    return {
        "hash": tx.get("hash"),
        "timestamp": ts_to_iso(tx.get("timeStamp")),
        "from": tx.get("from"),
        "to": tx.get("to"),
        "value": to_decimal(tx.get("value"), decimals=18),
        "token": "ETH",
        "token_symbol": "ETH",
        "token_decimals": 18,
        "is_error": tx.get("isError"),
        "gas": int(tx.get("gas", "0")),
        "gas_price": int(tx.get("gasPrice", "0")),
        "blockNumber": int(tx.get("blockNumber", "0"))
    }

def normalize_erc20_tx(tx: Dict) -> Dict:
    """
    Convert token tx to normalized row
    """
    decimals = int(tx.get("tokenDecimal") or 0)
    return {
        "hash": tx.get("hash"),
        "timestamp": ts_to_iso(tx.get("timeStamp")),
        "from": tx.get("from"),
        "to": tx.get("to"),
        "value": to_decimal(tx.get("value"), decimals=decimals),
        "token": tx.get("contractAddress"),
        "token_symbol": tx.get("tokenSymbol"),
        "token_decimals": decimals,
        "is_error": "0",
        "gas": None,
        "gas_price": None,
        "blockNumber": int(tx.get("blockNumber", "0"))
    }

def merge_and_sort(rows: List[Dict]) -> List[Dict]:
    return sorted(rows, key=lambda r: r["blockNumber"])
