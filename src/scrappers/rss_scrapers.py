import xml.etree.ElementTree as ET
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Iterable

from ..tools.logger import init_logger

logger = init_logger("dataconverter", 20)


@dataclass(eq=False)
class Scraper:
    channel_elements: Iterable[str]
    item_elements: Iterable[str]
    data: str
    limit: int = 10
    tree: ET.Element = field(init=False)

    @abstractmethod
    def __post_init__(self) -> None:
        self.tree = ET.fromstring(self.data)

    def scrap_channel_data(self):
        data = {}
        for i in self.channel_elements:
            root = self.tree.find(f"./channel/{i}")
            if root and root.text:
                data[i] = root.text[:120]
        return data

    def scrap_items_data(self):
        res = []
        root = self.tree.findall("./channel/item")

        if self.limit is None:
            self.limit = len(root)

        for i in range(min(self.limit, len(root))):
            dict_of_data = {}
            for j in self.item_elements:
                found = root[i].find(f"./{j}")
                if found and found.text:
                    dict_of_data[j] = found.text[:120]
            res.append(dict_of_data)
        return res

    def scrap_all_data(self):
        channel_data = self.scrap_channel_data()
        items_data = self.scrap_items_data()
        channel_data["items"] = items_data
        return channel_data
