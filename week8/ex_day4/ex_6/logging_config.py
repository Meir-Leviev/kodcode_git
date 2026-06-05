import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)-8s | %(name)s (%(filename)s:%(lineno)d) -> %(message)s",
                    handlers=[
                        logging.FileHandler("server.log"),
                        logging.StreamHandler()
                    ]
                    )

logger = logging.getLogger(__name__)
