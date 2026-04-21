import logging
import os

def setup_logger():
    """
    Sets up the logger to log to logs/app.log with appropriate format.
    """
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)