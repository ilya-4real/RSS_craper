from abc import ABC, abstractmethod

class AbstractJsonWriter(ABC):
    @abstractmethod
    def write_json(*data):
        raise NotImplementedError
    

class AbstractTxtWriter(ABC):
    @abstractmethod
    def write_txt(data, filename):
        raise NotImplementedError
    