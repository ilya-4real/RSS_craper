import xml.etree.ElementTree as ET
from dataparser import DataParser
from .absctract_scrapper import AbstractScrapper



RSS_CHANNEL_ITEMS = ("title", "link", "description", "category", "language"
                    "lastBuildDate", "managingEditor", "pubDate")

RSS_ITEM_ITEMS = ("title", "author", "pubDate", "link", "category", "description")

class ScrapperInit:
    def __init__(self, parser: DataParser) -> None:
        self.parser = parser
        self.data = parser.get_data()
        self.tree = ET.fromstring(self.data)


class ChannelScraper(AbstractScrapper, ScrapperInit):

    def scrap(self):
        """function that scraps data about channel"""
        data = {}
        for i in RSS_CHANNEL_ITEMS:
            root = self.tree.find(f"./channel/{i}")
            if root is not None:
                data[i] = root.text[:120]
        return data


class ItemsScrapper(AbstractScrapper, ScrapperInit):

    def scrap(self, limit: int = 10) -> list[dict]:
        """
        function that scraps items in the newsfeed
        :param limit: limit of items scraped
        :return: list(dict)
        """
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
    

class WholeRSScrapper:
    def __init__(self, parser: DataParser) -> None:
        self.channel_scrapper = ChannelScraper(parser)
        self.item_scrapper = ItemsScrapper(parser)

    def scrap_all_data(self, limit: int = 10) -> dict:
        channel_info = self.channel_scrapper.scrap()
        channel_info.update({"items" : self.item_scrapper.scrap(limit)})
        return channel_info