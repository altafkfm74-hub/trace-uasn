"""Optional trace logger (CSV)."""
from __future__ import annotations
import csv, os


def write_csv(path: str, rows: list, headers: list) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in rows:
            w.writerow(r)
