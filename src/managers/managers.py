from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from ..scrappers.rss_scrapers import (
    Scraper,
)
from ..tools.dataparser import AsyncDataParser, DataParser
from ..writers.writers import FileWriter, StdoutWRiter


@dataclass
class AbstractScraper(ABC):
    url: str
    channel_elements: Iterable[str]
    item_elements: Iterable[str]
    channel: bool = True
    items: bool = True
    items_limit: int = 10


@dataclass
class RSSCraper(AbstractScraper):
    def __post_init__(self):
        self.parser = DataParser(self.url)
        self.data = self.parser.get_data()
        self.scraper = Scraper(
            self.channel_elements,
            self.item_elements,
            self.data,
            self.items_limit,
        )

    def get_data(self):
        if self.channel and self.items:
            return self.scraper.scrap_all_data()
        elif self.channel:
            return self.scraper.scrap_channel_data()
        elif self.items:
            return self.scraper.scrap_items_data()

    def write_data(self, json: bool, path_to_dir: Path | None = None) -> None:
        data = self.get_data()
        match path_to_dir:
            case None:
                StdoutWRiter(json).write(data)
            case _:
                FileWriter(json).write(data)


@dataclass
class AsyncRSSCraper(AbstractScraper):
    def __post_init__(self):
        self.parser = AsyncDataParser(self.url)

    async def get_data(self):
        data = await self.parser.get_data()
        # print(data)
        scraper = Scraper(
            self.channel_elements,
            self.item_elements,
            data,
            self.items_limit,
        )
        if self.channel and self.items:
            return scraper.scrap_all_data()
        elif self.channel:
            return scraper.scrap_channel_data()
        elif self.items:
            return scraper.scrap_items_data()

    async def write_data(
        self, json: bool, path_to_dir: Path | None = None
    ) -> None:
        data = await self.get_data()
        match path_to_dir:
            case None:
                StdoutWRiter(json).write(data)
            case _:
                FileWriter(json).write(data)
