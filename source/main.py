import asyncio

from web.server import init_web_server
from misc.env import settings

async def main():
    await init_web_server(config=settings.web_config)

    while True:
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())