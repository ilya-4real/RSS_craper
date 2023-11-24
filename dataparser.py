from requests import get
from tools.logger import init_logger

logger = init_logger("data parser", 20)

class DataParser:
    def __init__(self, url) -> None:
        self.url = url

    def get_data(self):
        logger.info("getting data from external resource")
        data = get(self.url)
        return data.text
