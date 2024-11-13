import asyncio
from web.server import init_web_server
from misc.env import settings

async def main() -> None:
    """
    Initializes the web server with the specified configuration and
    keeps the application running indefinitely.

    The server will be configured based on settings provided in
    'settings.web_config' and will continue running with a sleep cycle.
    """
    await init_web_server(config=settings.web_config)

    # Keeps the application running indefinitely, with a 1-hour sleep interval.
    while True:
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())
