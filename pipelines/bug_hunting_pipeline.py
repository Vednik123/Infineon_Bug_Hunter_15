# pipelines/bug_hunting_pipeline.py

from agents import (
    ParserAgent,
    BugDetectorAgent,
    ExplanationAgent,
    CSVWriterAgent
)


class BugHuntingPipeline:

    def __init__(self, mcp_client):
        self.parser_agent = ParserAgent()
        self.bug_detector_agent = BugDetectorAgent(mcp_client)
        self.explanation_agent = ExplanationAgent(mcp_client)
        self.csv_writer_agent = CSVWriterAgent()

    def run(self, input_csv_path, output_csv_path):

        input_rows = self.parser_agent.run(input_csv_path)

        output_rows = []

        for row in input_rows:

            bug_line = self.bug_detector_agent.run(row)
            explanation = self.explanation_agent.run(row)

            output_rows.append({
                "ID": row.get("ID"),
                "Bug Line": bug_line,
                "Explanation": explanation
            })

        self.csv_writer_agent.run(output_csv_path, output_rows)
