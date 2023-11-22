# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        #>>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        #>>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        #>>> print("\\n".join(rss_parser(xml)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    # Your code goes here
    replaced_channel_title = xml.replace('title', 'feed', 2)
    channel_tags = ('feed', 'link', 'description', 'category', 'language'
                                                            'lastBuildDate', 'managingEditor', 'pubDate')

    item_tags = ('title', 'author', 'pubDate', 'link', 'category', 'description')

    root = ET.fromstring(replaced_channel_title)
    parsed_data = []

    for i in channel_tags:
        data = root.find(f'./channel/{i}')
        if data is not None:
            parsed_data.append(f'{i.capitalize()} : {data.text}')
        else:
            continue

    item_root = root.findall('./channel/item')  # finding all channel items

    if limit is None:   # setting up the limit
        limit = len(item_root)

    for i in range(min(limit, len(item_root))):
        res = []
        for j in item_tags:
            found = item_root[i].find(f'./{j}')
            if found is not None:
                res.append(f'{j.capitalize()} : {found.text}')
        parsed_data.append('')
        parsed_data.extend(res)

    return parsed_data


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    source = 'https://news.yahoo.com/rss'
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(source).text
    try:
        print(type(rss_parser(xml, args.limit, args.json)))
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
