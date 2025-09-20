# src/visualizer.py
import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Dict

def draw_graph(G, max_nodes=30, figsize=(12,8), title="Counterparty graph"):
    plt.figure(figsize=figsize)
    # if too many nodes, extract top by degree
    if G.number_of_nodes() > max_nodes:
        degrees = sorted(G.degree(weight="weight"), key=lambda x: x[1], reverse=True)[:max_nodes]
        nodes = [n for n,_ in degrees]
        sg = G.subgraph(nodes).copy()
    else:
        sg = G
    pos = nx.spring_layout(sg, k=0.7)
    weights = [d.get("weight", 1) for _,_,d in sg.edges(data=True)]
    nx.draw_networkx_nodes(sg, pos, node_size=300)
    nx.draw_networkx_edges(sg, pos, width=[max(0.5, float(w)/max(weights)*5) if weights else 1 for w in weights], arrowsize=12)
    nx.draw_networkx_labels(sg, pos, font_size=8)
    plt.title(title)
    plt.axis("off")
    plt.show()

def timeline_summary(rows):
    import pandas as pd
    df = pd.DataFrame(rows)
    df['date'] = pd.to_datetime(df['timestamp'])
    daily = df.groupby(df['date'].dt.date).agg({"value": "sum", "hash": "count"}).rename(columns={"hash":"tx_count"})
    print(daily.tail(20))
