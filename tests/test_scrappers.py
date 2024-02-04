import pytest
from src.scrappers.rss_scrapers import ChannelScraper, ItemsScraper
from src.tools import dataparser

MOCK_DATA = b"""<rss version="2.0">
<channel>
    <title>Yahoo News - Latest News Headlines</title>
    <link>https://www.yahoo.com/news</link>
    <description>
The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.
</description>
<language>en-US</language>
<copyright>Copyright (c) 2024 Yahoo! Inc. All rights reserved</copyright>
<pubDate>Sun, 04 Feb 2024 15:20:07 -0500</pubDate>
<ttl>5</ttl>
<image>
<title>Yahoo News - Latest News Headlines</title>
<link>https://www.yahoo.com/news</link>
<url>
http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png
</url>
</image>
<item>
<title>A woman stole a memory card from a truck. The gruesome footage is now key to an Alaska murder trial</title>
<link>https://news.yahoo.com/stolen-digital-memory-card-gruesome-050139352.html</link>
<pubDate>2024-02-04T05:01:39Z</pubDate>
<source url="https://apnews.com/">Associated Press</source>
<guid isPermaLink="false">stolen-digital-memory-card-gruesome-050139352.html</guid>
</item>
</channel>
</rss>"""

expected_channel = {
    "title": "Yahoo News - Latest News Headlines",
    "link": "https://www.yahoo.com/news",
    "description": "\nThe latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.",
    "pubDate": "Sun, 04 Feb 2024 15:20:07 -0500",
    "language": "en-US",
}

expected_item = [
    {
        "title": "A woman stole a memory card from a truck. The gruesome footage is now key to an Alaska murder trial",
        "link": "https://news.yahoo.com/stolen-digital-memory-card-gruesome-050139352.html",
        "pubDate": "2024-02-04T05:01:39Z",
    }
]


@pytest.fixture
def mock_dataparser(mocker):
    parser = dataparser.DataParser("https://yahoo.com/news/rss")
    mocker.patch.object(parser, "get_data", return_value=MOCK_DATA)
    return parser.get_data()


def test_scraper_init_with_parser(mock_dataparser):
    scraper = ChannelScraper(mock_dataparser)
    assert scraper.tree is not None


def test_scraper_init_with_raw_data(mock_dataparser):
    scraper = ChannelScraper(MOCK_DATA)  # type: ignore
    assert scraper.tree is not None


def test_channel_scrap(mock_dataparser):
    scraper = ChannelScraper(mock_dataparser)
    assert scraper.scrap() == expected_channel


def test_itme_scrap(mock_dataparser):
    scraper = ItemsScraper(mock_dataparser)
    assert scraper.scrap() == expected_item
