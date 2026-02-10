# utils/csv_loader.py

import csv
from typing import List, Dict
from utils.logger import get_logger

logger = get_logger(__name__)

REQUIRED_COLUMNS = {"ID", "Code"}

OPTIONAL_COLUMNS = {
    "Context",
    "Explanation",
    "Correct Code"
}

def load_input_csv(file_path: str) -> List[Dict]:
    """
    Loads input CSV provided by organizers.

    Expected Columns:
    ID | Explanation | Context | Code | Correct Code

    Returns:
        [
          {
            "id": str,
            "code": str,
            "context": str,
            "gt_explanation": str,
            "correct_code": str
          }
        ]
    """

    logger.info(f"Loading input CSV: {file_path}")
    rows = []

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            raise ValueError(
                f"CSV must contain columns: {REQUIRED_COLUMNS}"
            )

        for row in reader:
            rows.append({
                "id": row.get("ID"),
                "code": row.get("Code", "").strip(),
                "context": row.get("Context", "").strip(),
                "gt_explanation": row.get("Explanation", "").strip(),
                "correct_code": row.get("Correct Code", "").strip()
            })

    logger.info(f"Loaded {len(rows)} code snippets")
    return rows
