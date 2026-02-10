class BugDetectorAgent:

    def __init__(self, mcp_client=None):
        self.mcp = mcp_client

    def run(self, row):

        code = row.get("Code", "")
        correct_code = row.get("Correct Code", "")

        code_lines = code.splitlines()
        correct_lines = correct_code.splitlines()

        max_len = max(len(code_lines), len(correct_lines))

        bug_lines = []

        for i in range(max_len):
            c1 = code_lines[i].strip() if i < len(code_lines) else ""
            c2 = correct_lines[i].strip() if i < len(correct_lines) else ""

            if c1 != c2:
                bug_lines.append(str(i + 1))   # line numbers start from 1

        # return comma separated line numbers (strings only)
        return ",".join(bug_lines)
