import argparse
from converter import convert
from rss_scraper import Scraper


def main():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
    #parser.add_argument('source', help='RSS URL')
    parser.add_argument('--json', action='store_true', help='print result as JSON in stdout.')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter is provided.')
    args = parser.parse_args()

    scrap = Scraper('https://news.yahoo.com/rss')
    channel = scrap.scrap_channel()
    items = scrap.scrap_item(args.limit)

    # git testing comment aaa
    for key, value in channel.items():
        print(f'{key} : {value}.')

    for i in items:
        for key, value in i.items():
            if key == 'link':
                print()
            print(f'{key} : {value}')
            # if key == 'link':
            #     print()
        print()

    if args.json:
        channel['items'] = items
        convert(channel, 'data.json')


if __name__ == '__main__':
    main()
