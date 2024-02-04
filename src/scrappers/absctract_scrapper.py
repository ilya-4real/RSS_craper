from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from typing import Union

from ..tools.dataparser import DataParser


class AbstractScraper(ABC):
    def __init__(self, data: Union[DataParser, str]) -> None:
        if isinstance(data, DataParser):
            self.parser = data
            data = self.parser.get_data()
        else:
            data = data
        self.tree = ET.fromstring(data)

    @abstractmethod
    def scrap():
        raise NotImplementedError
