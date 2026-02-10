# utils/logger.py

import logging
import os
from datetime import datetime

# Create logs directory if not present
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file with timestamp
LOG_FILE = os.path.join(
    LOG_DIR,
    f"agentic_bug_hunter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# Global logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.
    
    Usage:
        logger = get_logger(__name__)
        logger.info("Message")
    """
    return logging.getLogger(name)
