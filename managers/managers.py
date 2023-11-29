from ..tools.argumentparser import get_cli_arguments
from ..tools.dataparser import DataParser
from ..scrappers.rss_scrapers import ChannelScraper, ItemsScraper, AllDataScraper
from ..writers.writers import CliWriter, FileWriter
from .abstract_manager import AbstractManager, AbstractStrategyChooser


class StrategyChooser(AbstractStrategyChooser):
    def __init__(self, url: str) -> None:
        self.parser = DataParser(url)

    def set_writing_strategy(self, file: bool, json: bool) -> None:
        if file:
            self.writing_strategy = FileWriter(json)
        else:
            self.writing_strategy = CliWriter(json)
     
    def set_scraping_strategy(
            self, 
            channel: bool = True, 
            items: bool = True, 
            limit: int = 10
            ) -> None:
        if channel and not items:
            self.scraping_strategy = ChannelScraper(self.parser)
        elif not channel and items:
            self.scraping_strategy = ItemsScraper(self.parser, limit)
        else:
            self.scraping_strategy = AllDataScraper(self.parser, limit)


class CliRSScraper(AbstractManager, StrategyChooser):
    def __init__(self) -> None:
        self.cli_arguments = get_cli_arguments()
        self.parser = DataParser(self.cli_arguments.source)
        self.set_writing_strategy(self.cli_arguments.file, self.cli_arguments.json)
        self.set_scraping_strategy(
            self.cli_arguments.channel,
            self.cli_arguments.items,
            self.cli_arguments.limit,
            )

    def write_data(self) -> None:
        data = self.scraping_strategy.scrap()
        self.writing_strategy.write(data)
    

class RSScraper(AbstractManager, StrategyChooser):
    def __init__(self, source: str) -> None:
        self.parser = DataParser(source)

    def write_data(
            self, 
            file: bool = True, 
            json: bool = False, 
            channel: bool = True, 
            items: bool = True, 
            limit: int = 10) -> None:
        self.set_writing_strategy(file, json)
        self.set_scraping_strategy(channel, items, limit)
        data = self.scraping_strategy.scrap()
        self.writing_strategy.write(data)

    def get_data(self, channel: bool = True, items: bool = True, limit: int = 10) -> dict:
        self.set_scraping_strategy(channel, items, limit)
        return self.scraping_strategy.scrap()
