from abc import ABC, abstractmethod
from dataparser import DataParser
import xml.etree.ElementTree as ET

class AbstractScrapper(ABC):
    def __init__(self, parser: DataParser) -> dict:
        self.parser = parser
        self.data = parser.get_data()
        self.tree = ET.fromstring(self.data)

    @abstractmethod
    def scrap():
        raise NotImplementedError