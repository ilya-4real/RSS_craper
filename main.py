import argparse
from scrappers.rss_scrapers import RSScrapper, ChannelScraper, ItemsScrapper
from dataparser import DataParser
from writers.writers import Writer
from tools.argumentparser import get_cli_arguments
from tools.logger import init_logger

logger = init_logger("scrapper", 20) 

debug_args = {
    "json": True,
    "source": "https://news.yahoo.com/rss",
    "limit": 2,
    "filename": None,
}

def main():
    cli_arguments = get_cli_arguments()
    data_parser = DataParser(cli_arguments.source)
    if cli_arguments.items and not cli_arguments.channel:
        scrapper = ItemsScrapper(data_parser)
    elif not cli_arguments.items and cli_arguments.channel:
        scrapper = ChannelScraper(data_parser)
    else:
        scrapper = RSScrapper(data_parser)
    scrapped_data = scrapper.scrap(cli_arguments.limit)
    writer = Writer(cli_arguments.filename, cli_arguments.json)
    writer.write(scrapped_data)


def debug_main():
    cli_arguments = debug_args
    data_parser = DataParser(cli_arguments["source"])
    rss_scrapper = RSScrapper(data_parser)
    scrapped_data = rss_scrapper.scrap_all_data(cli_arguments["limit"])
    writer = Writer(cli_arguments["filename"], cli_arguments["json"])
    writer.write(scrapped_data)

if __name__ == '__main__':
    main()
