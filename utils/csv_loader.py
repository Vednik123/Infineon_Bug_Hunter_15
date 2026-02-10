# utils/csv_loader.py

import csv


def load_input_csv(path):
    """
    Loads input CSV and returns list of dict rows.
    """

    rows = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            rows.append(row)

    return rows
