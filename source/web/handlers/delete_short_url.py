from aiohttp import web
from source.database.methods.delete import delete_short_url

async def delete_url(request: web.Request) -> web.Response:
    """
    Deletes a shortened URL from the database based on the provided short code.

    Args:
        request (web.Request): The incoming HTTP request containing 'short_code' in the URL.

    Returns:
        web.Response: Success message if deleted, or an error if the short code is not found.
    """
    short_code = request.match_info.get('short_code')

    # Attempt to delete the URL entry from the database
    if delete_short_url(short_code):
        return web.Response(text="Short URL deleted successfully", status=200)
    else:
        return web.Response(text="Short URL not found", status=404)
