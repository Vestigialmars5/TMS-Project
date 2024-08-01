import logging

logging.basicConfig(level=logging.ERROR)


def log_error(error):
    logging.error(f"An error occurred: {str(error)}", exc_info=True)
