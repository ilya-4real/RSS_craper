from abc import ABC, abstractmethod
from dataparser import DataParser
import xml.etree.ElementTree as ET
from typing import Union

class AbstractScrapper(ABC):
    def __init__(self, data: Union[DataParser, str]) -> dict:
        if type(data) == DataParser:
            self.parser = data
            self.data = data.get_data()
        else:
            self.data = data
        self.tree = ET.fromstring(self.data)

    @abstractmethod
    def scrap():
        raise NotImplementedError