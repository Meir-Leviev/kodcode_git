# 5
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')

# 6


def process_payment(user_id, amount):
    logger.info(f'Starting payment for user {user_id}')
    if amount <= 0:
        logger.error('Invalid amount')
        return
    if amount > 10000:
        logger.warning('Large transaction')
    logger.info(f'Payment of {amount} completed for user {user_id}')
