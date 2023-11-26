from abc import ABC, abstractmethod


class AbstractManager(ABC):
    @abstractmethod
    def get_data():
        raise NotImplementedError