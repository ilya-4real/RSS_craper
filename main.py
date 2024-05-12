import asyncio

from src import config

from .src.managers.managers import AsyncRSSCraper
from 


async def main():
    scr = AsyncRSSCraper(
        "https://finance.yahoo.com/rss/",
        config.RSS_CHANNEL_TAGS,
        config.RSS_ITEM_TAGS,
    )
    task = asyncio.create_task(scr.get_data())
    data = await task
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
