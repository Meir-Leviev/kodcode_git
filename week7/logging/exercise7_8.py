import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger = logging.getLogger('payments')
formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )
file_handler = logging.FileHandler('logs.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def user_login():
    logger.info('staring')
    something = 0
    if not something:
        logger.error('something not good')
        return
    logger.info('done')


# 8
def read_config(filepath):
    logger.debug('starting')
    try:
        with open(filepath) as f:
            data = f.read
        logger.info('success')
        return data
    except FileNotFoundError:
        logger.exception('not good')
        return None
