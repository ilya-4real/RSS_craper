from typing import Mapping

from ..tools.dataparser import DataParser
from ..tools.logger import init_logger
from ..config import RSS_CHANNEL_TAGS, RSS_ITEM_TAGS
from .absctract_scrapper import AbstractScraper


logger = init_logger("dataconverter", 20)


class ChannelScraper(AbstractScraper):
    def scrap(self) -> dict[str, str]:
        logger.info("converting channel data")
        data = {}
        for i in RSS_CHANNEL_TAGS:
            root = self.tree.find(f"./channel/{i}")
            if root is not None:
                data[i] = root.text[:120]  # type: ignore
        return data


class ItemsScraper(AbstractScraper):
    def __init__(self, data: DataParser | str, limit: int | None = 10) -> None:
        super().__init__(data)
        self.limit = limit

    def scrap(self) -> list[dict[str, str]]:
        logger.info("converting items data")
        res = []
        root = self.tree.findall("./channel/item")

        if self.limit is None:
            self.limit = len(root)

        for i in range(min(self.limit, len(root))):
            dict_of_data = {}
            for j in RSS_ITEM_TAGS:
                found = root[i].find(f"./{j}")
                if found is not None:
                    dict_of_data[j] = found.text[:120]  # type: ignore
            res.append(dict_of_data)
        return res


class AllDataScraper:
    def __init__(self, parser: DataParser, limit: int | None) -> None:
        self.parser = parser
        data = self.parser.get_data()
        self.channel_scraper = ChannelScraper(data)
        self.items_scraper = ItemsScraper(data, limit)

    def scrap(self) -> Mapping[str, str | list[dict[str, str]]]:
        channel_data = self.channel_scraper.scrap()
        items_data = self.items_scraper.scrap()
        channel_data.update({"items": items_data})  # type: ignore
        return channel_data
