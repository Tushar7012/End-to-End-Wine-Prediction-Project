import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent))  # Adds 'src' to sys.path

from src.mlProject import logger  # Now import your modules

logger.info("Main script started...")