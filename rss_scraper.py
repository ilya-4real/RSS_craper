import xml.etree.ElementTree as ET
from dataparser import DataParser


RSS_CHANNEL_ITMES = ("title", "link", "description", "category", "language"
                    "lastBuildDate", "managingEditor", "pubDate")

RSS_ITEM_ITEMS = ("title", "author", "pubDate", "link", "category", "description")


class Scraper:
    def __init__(self, parser: DataParser) -> dict:
        self.parser = parser
        self.data = parser.get_data()
        self.tree = ET.fromstring(self.data)
        

    def scrap_channel(self):
        """function that scraps data about channel"""
        data = {}
        for i in RSS_CHANNEL_ITMES:
            root = self.tree.find(f"./channel/{i}")
            if root is not None:
                data[i] = root.text[:120]
        return data


    def scrap_item(self, limit: int = 10) -> list[dict]:
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
    
