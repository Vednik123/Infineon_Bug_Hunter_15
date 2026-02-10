# utils/validators.py

REQUIRED_COLUMNS = [
    "ID",
    "Context",
    "Code",
    "Correct Code",
    "Explanation"
]


def validate_input_row(row):
    """
    Checks if a CSV row contains all required columns.
    """

    for col in REQUIRED_COLUMNS:
        if col not in row or row[col] is None:
            return False, f"Missing column: {col}"

    return True, None
