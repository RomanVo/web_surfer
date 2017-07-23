import logging
import os


class SimpleLogger:
    """
    Simple logger implementation for surfer
    """
    LOG_FILENAME = os.path.expanduser('~') + '/log/main.log'
    logger = logging.getLogger(__name__)

    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler(self.LOG_FILENAME)
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(handler)

    def log_info(self, message):
        """
        Log INFO message
        @param message: message string
        """
        self.logger.info(message)
