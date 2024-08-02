import logging
import os
from logging.handlers import RotatingFileHandler


# Logging configuration for the server
def setup_logging(log_dir):
    try:
        os.makedirs(log_dir)
        print(f"Logs directory created at: {log_dir}")
    except OSError:
        pass
    

    # General server logging
    server_log = RotatingFileHandler(
        os.path.join(log_dir, "server.log"), maxBytes=1000000, backupCount=5)
    server_log.setLevel(logging.INFO)
    server_log.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # Error logging
    error_log = RotatingFileHandler(
        os.path.join(log_dir, "error.log"), maxBytes=1000000, backupCount=5)
    error_log.setLevel(logging.ERROR)
    error_log.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # Add the handlers to the logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(server_log)
    logger.addHandler(error_log)

    return logger
