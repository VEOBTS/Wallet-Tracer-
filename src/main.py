# src/__main__.py
import argparse
from .fetcher import fetch_normal_txs, fetch_erc20_txs
from .normalizer import normalize_normal_tx, normalize_erc20_tx, merge_and_sort
from .storage import save_rows_csv, save_rows_sqlite
from .graph_builder import build_counterparty_graph
from .visualizer import draw_graph, timeline_summary

def main():
    parser = argparse.ArgumentParser(description="Wallet Transaction Tracer")
    parser.add_argument("address", help="wallet address (0x...)")
    parser.add_argument("--save-csv", action="store_true")
    parser.add_argument("--build-graph", action="store_true")
    args = parser.parse_args()
    addr = args.address

    print(f"[+] Fetching normal txs for {addr} ...")
    normal = fetch_normal_txs(addr)
    print(f"[+] Fetched {len(normal)} normal txs")
    print(f"[+] Fetching token transfers for {addr} ...")
    tokens = fetch_erc20_txs(addr)
    print(f"[+] Fetched {len(tokens)} token txs")

    rows = []
    for t in normal:
        rows.append(normalize_normal_tx(t))
    for t in tokens:
        rows.append(normalize_erc20_tx(t))

    rows = merge_and_sort(rows)
    print(f"[+] Total normalized rows: {len(rows)}")

    if args.save_csv:
        path = save_rows_csv(rows)
        print(f"[+] CSV saved: {path}")

    if args.build_graph:
        print("[+] Building counterparty graph ...")
        G = build_counterparty_graph(rows, addr)
        print(f"[+] Graph nodes: {G.number_of_nodes()}, edges: {G.number_of_edges()}")
        draw_graph(G, title=f"Counterparty graph for {addr}")
        print("[+] Timeline summary (recent days):")
        timeline_summary(rows)

if __name__ == "__main__":
    main()
