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

1. Clone this repo via: 

~~~sh
git clone https://github.com/ilya-4real/RSS-scraper.git
~~~

2. Activate virtual env:

~~~sh
python -m venv venv
source venv/bin/activate
~~~

3. Install required packages:

~~~sh
pip install -r requirements.txt
~~~

<h3>Everything is ready to parse)</h3>

<h1>Usage</h1>
You can easily view all available arguments for the parser via: 

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
