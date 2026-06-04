import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s | %(funcName)s (%(filename)s) | %(message)s",
    handlers=[
        logging.FileHandler("server.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

