import logging
import logging.handlers
import os

def _ensure_log_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
LOG_FILE = os.path.join(LOG_DIR, 'renamer.log')

_ensure_log_dir(LOG_FILE)

def configure_logger(level=logging.INFO):
    """Configure and return the root logger for the project."""
    logger = logging.getLogger('fileRenamer')
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(ch_formatter)
    logger.addHandler(ch)

    # Rotating file handler
    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)

    return logger


# Module-level logger instance
logger = configure_logger()

def get_logger(name: str | None = None):
    if name:
        return logging.getLogger(f'fileRenamer.{name}')
    return logger
