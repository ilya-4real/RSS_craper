import xml.etree.ElementTree as ET
from dataparser import DataParser
from abc import ABC, abstractmethod


RSS_CHANNEL_ITEMS = ("title", "link", "description", "category", "language"
                    "lastBuildDate", "managingEditor", "pubDate")

RSS_ITEM_ITEMS = ("title", "author", "pubDate", "link", "category", "description")


class AbstractScraper(ABC):
    def __init__(self, parser: DataParser) -> dict:
        self.parser = parser
        self.raw_data = parser.get_data()
        self.tree = ET.fromstring(self.raw_data)

    @abstractmethod
    def scrap(self, data):
        raise NotImplementedError
        

class AbsctractCombinedScraper(ABC):
    @abstractmethod
    def get_combined_info():
        raise NotImplementedError


class ItemScrapper(AbstractScraper):
    def __init__(self, parser: DataParser, limit: int = 10) -> dict:
        super().__init__(parser)
        self.limit = limit

    def scrap(self):

        """
        function that scraps items in the newsfeed
        :param limit: limit of items scraped
        :return: list(dict)
        """
 
        res = []
        root = self.tree.findall("./channel/item")

        if self.limit is None:
            limit = len(root)

        for i in range(min(self.limit, len(root))):
            dict_of_data = {}
            for j in RSS_ITEM_ITEMS:
                found = root[i].find(f"./{j}")
                if found is not None:
                    dict_of_data[j] = found.text[:120]
            res.append(dict_of_data)
        return res
    

class ChannelScrapper(AbstractScraper):
    def __init__(self, parser: DataParser) -> dict:
        super().__init__(parser)

    def scrap(self):

        """function that scraps data about channel"""

        data = {}
        for i in RSS_CHANNEL_ITEMS:
            root = self.tree.find(f"./channel/{i}")
            if root is not None:
                data[i] = root.text[:120]
        return data
    

class WholeScrapper(AbsctractCombinedScraper):
    def __init__(self, parser: DataParser, limit: int = 10) -> None:
        self.parser = parser
        self.channel_scrapper = ChannelScrapper(parser)
        self.items_scrapper = ItemScrapper(parser, limit)

    def get_combined_info(self): 

        """method that scraps whole channel info: channel and items info"""

        channel_info = self.channel_scrapper.scrap()
        items_info = self.items_scrapper.scrap()

        channel_info.update({"items": items_info})

        return channel_info