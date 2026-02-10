class ExplanationAgent:

    def __init__(self, mcp_client):
        self.mcp = mcp_client

    def run(self, row):

        buggy = row.get("Code", "")
        correct = row.get("Correct Code", "")
        context = row.get("Context", "")

        # ---- ask MCP for related documentation ----
        query = f"""
{context}

Buggy code:
{buggy}

Correct code:
{correct}

Explain the API or behavior related to this change.
"""

        doc_hint = ""

        # use MCP only if available
        if self.mcp is not None:
            try:
                results = self.mcp.search_documents(query)
                if results:
                    doc_hint = results[0].get("text", "")
            except Exception:
                # MCP unavailable or failed
                doc_hint = ""

        # ---- now generate explanation using retrieved context ----
        buggy_lines = buggy.splitlines()
        correct_lines = correct.splitlines()

        max_len = max(len(buggy_lines), len(correct_lines))

        explanations = []

        for i in range(max_len):
            b = buggy_lines[i].strip() if i < len(buggy_lines) else ""
            c = correct_lines[i].strip() if i < len(correct_lines) else ""

            if b != c:
                explanations.append(
                    f"Line {i+1} is incorrect. "
                    f"The buggy statement '{b}' should be replaced with '{c}'. "
                    + (f"According to the documentation: {doc_hint}" if doc_hint else "")
                )

        if not explanations:
            return "No functional difference found based on documentation."

        # must return string
        return " ".join(explanations)
