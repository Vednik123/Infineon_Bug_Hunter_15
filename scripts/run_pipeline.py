import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from orchestrator.main_orchestrator import main

if __name__ == "__main__":
    main()
