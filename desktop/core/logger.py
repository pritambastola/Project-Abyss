"""
Project-Abyss Logging Service

Provides centralized logging for the entire application.

Only this module should directly use Loguru.
Every other module imports the configured logger from here.
"""

from pathlib import Path

from loguru import logger

# --------------------------------------------------
# Paths
# --------------------------------------------------

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "project_abyss.log"

# --------------------------------------------------
# Logger Configuration
# --------------------------------------------------

logger.remove()

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level:<8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> "
        "- <level>{message}</level>"
    ),
)

logger.add(
    LOG_FILE,
    level="DEBUG",
    rotation="10 MB",
    retention="14 days",
    compression="zip",
    encoding="utf-8",
)

__all__ = ["logger"]