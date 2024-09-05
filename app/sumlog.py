import logging
import sys


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')


class SLogger:
    LEVELS = []

    def __init__(self):
        self.fileLogger = SLogger.get_file_slogger()
        self.streamLogger = SLogger.get_stream_logger()

    def log(self, msg, level=logging.INFO, file=True, stream=True):
        self.fileLogger.info(msg)
        self.streamLogger.info(msg)

    @staticmethod
    def get_file_slogger():


        # create logger with 'spam_application'
        logger = logging.getLogger('reporter_logger')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('logs\\reporters.log')
        fh.setLevel(logging.DEBUG)
        # # create console handler with a higher log level
        # ch = logging.StreamHandler(sys.stdout)
        # ch.setLevel(logging.INFO)
        # # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        # logger.addHandler(ch)
        return logger

    @staticmethod
    def get_stream_logger():
        logger = logging.getLogger('reporter_logger')
        logger.setLevel(logging.INFO)
        # create console handler with a higher log level
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        logger.addHandler(ch)
        return logger



# def some_function():
#     module_logger.info('received a call to "some_function"')