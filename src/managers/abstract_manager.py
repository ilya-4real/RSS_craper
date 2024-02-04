from abc import ABC, abstractmethod


class AbstractManager(ABC):
    @abstractmethod
    def write_data():
        raise NotImplementedError
    

class AbstractStrategyChooser(ABC):
    @abstractmethod 
    def set_writing_strategy():
        raise NotImplementedError
    
    @abstractmethod 
    def set_scraping_strategy():
        raise NotImplementedError