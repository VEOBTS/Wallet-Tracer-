# src/graph_builder.py
import networkx as nx
from typing import List, Dict
from collections import defaultdict

def build_counterparty_graph(rows: List[Dict], address: str, weight_by="sum_value"):
    """
    rows: normalized tx rows
    address: target wallet (lowercase)
    weight_by: 'sum_value' or 'count'
    """
    G = nx.DiGraph()
    address = address.lower()
    # aggregate edges
    edge_agg = defaultdict(lambda: {"value": 0, "count": 0})
    for r in rows:
        from_addr = (r["from"] or "").lower()
        to_addr = (r["to"] or "").lower()
        value = float(r.get("value") or 0.0)
        # consider edges involving our address
        if from_addr == address:
            key = (from_addr, to_addr)
            edge_agg[key]["value"] += value
            edge_agg[key]["count"] += 1
        elif to_addr == address:
            key = (from_addr, to_addr)
            edge_agg[key]["value"] += value
            edge_agg[key]["count"] += 1
        # optionally include other interactions? for now edges touching address

    for (u,v), meta in edge_agg.items():
        weight = meta["value"] if weight_by=="sum_value" else meta["count"]
        G.add_node(u)
        G.add_node(v)
        G.add_edge(u, v, weight=weight, tx_count=meta["count"], total_value=meta["value"])

    return G
