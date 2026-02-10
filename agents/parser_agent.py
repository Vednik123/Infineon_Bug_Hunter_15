# agents/parser_agent.py

from utils.csv_loader import load_input_csv

class ParserAgent:

    def run(self, input_csv_path: str):
        """
        Loads the input CSV and returns list of rows.
        """
        rows = load_input_csv(input_csv_path)
        return rows
    