import csv
import os


class CSVWriterAgent:

    def run(self, output_path, rows):
        """
        rows:
        [
            {
                "ID": ...,
                "Bug Line": ...,
                "Explanation": ...
            }
        ]
        """

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["ID", "Bug Line", "Explanation"]
            )
            writer.writeheader()
            writer.writerows(rows)
