import argparse
from converter import convert_xml_to_json
from rss_scraper import Scraper
from dataparser import DataParser
from writers.writers import Writer


def get_cli_arguments():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS scrapper.')
    parser.add_argument('source', help='RSS URL')
    parser.add_argument('--json', action='store_true', help='print result as JSON in stdout.')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter is provided.')
    parser.add_argument('--filename',
                         type=str, help='write RSS data to file news. if json is True .json format needed else .xml format',
                           default=None)
    return parser.parse_args()

def debug_args():
    args = {
        "source": "https://news.yahoo.com/rss",
        "json": True,
        "filename": None,
        "limit": 10
    }
    return args


def main():
    cli_arguments = get_cli_arguments()
    data_parser = DataParser(cli_arguments.source)
    rss_scrapper = Scraper(data_parser)

    if cli_arguments.json:
        channel_data = convert_xml_to_json(rss_scrapper.scrap_channel())
        items_data = convert_xml_to_json(rss_scrapper.scrap_item())
    else:
        channel_data = rss_scrapper.scrap_channel()
        items_data = rss_scrapper.scrap_item(cli_arguments.limit)

    writer = Writer(cli_arguments.filename, cli_arguments.json)
    print(type(channel_data), type(items_data))
    
    writer.write(channel_data, items_data)


def debug_main():
    cli_arguments = debug_args()
    data_parser = DataParser(cli_arguments['source'])
    rss_scrapper = Scraper(data_parser)

    if cli_arguments['json']:
        channel_data = convert_xml_to_json(rss_scrapper.scrap_channel())
        items_data = convert_xml_to_json(rss_scrapper.scrap_item())
    else:
        channel_data = rss_scrapper.scrap_channel()
        items_data = rss_scrapper.scrap_item(cli_arguments['limit'])

    writer = Writer(cli_arguments['filename'], cli_arguments['json'])
    print(type(channel_data), type(items_data))
    
    writer.write(channel_data, items_data)



if __name__ == '__main__':
    main()
