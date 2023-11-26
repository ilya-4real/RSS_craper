from dataparser import DataParser
from .absctract_scrapper import AbstractScrapper
from tools.logger import init_logger
from typing import Union

logger = init_logger("dataconverter", 20)

RSS_CHANNEL_ITEMS = ("title", "link", "description", "category", "language"
                    "lastBuildDate", "managingEditor", "pubDate")

RSS_ITEM_ITEMS = ("title", "author", "pubDate", "link", "category", "description")


class ChannelScraper(AbstractScrapper):
    def scrap(self, limit):
        """function that scraps data about channel"""
        logger.info("converting channel data")
        data = {}
        for i in RSS_CHANNEL_ITEMS:
            root = self.tree.find(f"./channel/{i}")
            if root is not None:
                data[i] = root.text[:120]
        return data
        


class ItemsScrapper(AbstractScrapper):
    def scrap(self, limit: int = 10) -> list[dict]:
        """
        function that scraps items in the newsfeed
        :param limit: limit of items scraped
        :return: list(dict)
        """
        logger.info("converting items data")
        res = []
        root = self.tree.findall("./channel/item")

        if limit is None:
            limit = len(root)

        for i in range(min(limit, len(root))):
            dict_of_data = {}
            for j in RSS_ITEM_ITEMS:
                found = root[i].find(f"./{j}")
                if found is not None:
                    dict_of_data[j] = found.text[:120]
            res.append(dict_of_data)
        return res
    

class RSScrapper:
    def __init__(self, parser: DataParser, scraping_strategy: Union[ChannelScraper, ItemsScrapper]) -> None:
        self.data = parser.get_data()
        self.scraping_strategy = scraping_strategy(data=self.data)

    def scrap(self, limit: int = 10) -> dict:
        if not self.scraping_strategy:
            self.channel_scrapper = ChannelScraper(data=self.data)
            self.item_scrapper = ItemsScrapper(data=self.data)
            logger.info("converting all the data")
            channel_info = self.channel_scrapper.scrap()
            channel_info.update({"items" : self.item_scrapper.scrap(limit)})
            return channel_info
        elif type(self.scraping_strategy) == ItemsScrapper:
            return self.scraping_strategy.scrap(limit)
        else:
            return self.scraping_strategy.scrap()