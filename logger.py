import logging


def set_up_logger():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('This will get logged')
