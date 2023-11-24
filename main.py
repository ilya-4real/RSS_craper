import argparse
from scrappers.rss_scrapers import WholeRSScrapper
from dataparser import DataParser
from writers.writers import Writer
from tools.argumentparser import get_cli_arguments


def main():
    cli_arguments = get_cli_arguments()
    data_parser = DataParser(cli_arguments.source)
    rss_scrapper = WholeRSScrapper(data_parser)
    scrapped_data = rss_scrapper.scrap_all_data(cli_arguments.limit)
    writer = Writer(cli_arguments.filename, cli_arguments.json)
    writer.write(scrapped_data)


if __name__ == '__main__':
    main()
