<h1>Description </h1>
<p>This is a tiny well-designed tool that is helpful for parsing  RSS data. It uses only one external library "requests" for getting data from web. You can choose where you want to see a result of the parsing in file or terminal through providing --filename argument to main.py file.</p>

<h4 class="">benefits:</h4>
<ul>
<li>Easy to use</li>
<li>only one requirement</li>
<li>beautiful result</li>
</ul>


<h1>Requirements</h1>
<ul>
<li>Python 3.11</li>
<li>requests > 2.31</li>
</ul>

<h1 class="">Installation</h1>

1. create a directory, for example **rss_scraper**:

~~~sh
mkdir rss_scraper
~~~

2. Clone this repo inside the folder you created: 

~~~sh
cd rss_scraper
git clone https://github.com/ilya-4real/RSS-scraper.git
~~~

3. Activate virtual env:

~~~sh
python -m venv venv
source venv/bin/activate
~~~

3. Install required packages:

~~~sh
pip install -r requirements.txt
~~~

4. if you are going to write scraped data to a file, you have to create a directory named **data** next to directory with code:

~~~sh
mkdir data
~~~

if you are going to use this package as a cli program you can easily create a **main.py** file containing next code:

<h3>Everything is ready to parse)</h3>

<h1>Usage</h1>
<h3>First of all</h3>
you should choose how you will use this package

1. if you are gonna use it as a cli program you can easely create a **main.py** file next to the folder with code containing this:

~~~python
from rss_scraper import CliRSScraper

def main():
    manager = CliRSScraper()
    manager.write()

if __name__ == "__main__":
    main()
~~~

2. Or you can import RSScraper from this package and use as you wish. For example:

~~~python
from rss_scraper import RSScraper

manager = RSScraper("https://link_to_the_RSS_source.com")
manager.write_data() # this code will write scraped data to a file

# Or

manager.get_data() # this method will return a dictionary containing all scraped data
~~~


<h3>Configuration</h3>
if you are using this package as a cli program you can easily view all available arguments for the parser using this command:

~~~sh
main.py --help
~~~


Here is the output of the command above:

~~~sh
usage: main.py [-h] [--json] [--limit LIMIT] [--filename FILENAME] source

Pure Python command-line RSS scrapper.

positional arguments:
  source               RSS URL

options:
  -h, --help           show this help message and exit
  --json               write result as JSON
  --limit LIMIT        Limit news topics if this parameter is provided.
  --filename FILENAME  if provided the script will save result to a file with name in this argument
~~~

The result above is clear enough for further use.

<h1>Usage example</h1>

Command:

~~~sh
main.py "https://news.yahoo.com/rss" --json --limit 2
~~~

Result in terminal:

~~~sh
{
  "title": "Yahoo News - Latest News & Headlines",
  "link": "https://www.yahoo.com/news",
  "description": "The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.",
  "pubDate": "Wed, 22 Nov 2023 11:49:01 -0500"
"items": [
        {
          "title": "Putin says we must think how to stop 'the tragedy' of war in Ukraine",
          "pubDate": "2023-11-22T13:58:38Z",
          "link": "https://news.yahoo.com/putin-must-think-stop-tragedy-135838216.html"
        },
        {
          "title": "Police warn residents after \"extremely venomous\" green mamba escapes",
          "pubDate": "2023-11-22T12:39:49Z",
          "link": "https://news.yahoo.com/police-warn-residents-extremely-venomous-123949206.html"
        }]
}
~~~
