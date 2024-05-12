from abc import ABC

import httpx
from requests import get

from .logger import init_logger

logger = init_logger("data parser", 20)


class AbstractDataParser(ABC):
    def __init__(self, url: str) -> None:
        self.url = url


class DataParser(AbstractDataParser):
    def get_data(self) -> str:
        logger.info("getting data from external resource")
        data = get(self.url)
        return data.text


class AsyncDataParser(AbstractDataParser):
    async def get_data(self) -> str:
        async with httpx.AsyncClient() as client:
            data = await client.get(self.url)
        return data.text
