from rss_scraper import WholeScrapper
from dataparser import DataParser
from writers.writers import Writer
from tools import get_cli_arguments


def main():
    cli_arguments = get_cli_arguments()
    data_parser = DataParser(cli_arguments.source)
    rss_scrapper = WholeScrapper(data_parser, cli_arguments.limit)
    scrapped_data = rss_scrapper.get_combined_info()
    writer = Writer(cli_arguments.filename, cli_arguments.json)
    writer.write(scrapped_data)


if __name__ == '__main__':
    main()
