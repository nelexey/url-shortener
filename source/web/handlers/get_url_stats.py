import json
from aiohttp import web
from source.database.methods.read import get_url_stats


async def get_stats(request: web.Request) -> web.Response:
    """
    Retrieves statistics for a shortened URL based on the provided short code.

    Args:
        request (web.Request): The incoming HTTP request containing 'short_code' in the URL.

    Returns:
        web.Response: JSON response with statistics or an error if the short code is not found.
    """
    short_code = request.match_info.get('short_code')

    # Retrieve the URL stats from the database
    url_stats = get_url_stats(short_code)
    if url_stats:
        # Prepare the response with statistics
        response_data = {
            "original_url": url_stats.original_url,
            "clicks": url_stats.clicks,
            "created_at": url_stats.created_at.isoformat(),
        }
        return web.Response(text=json.dumps(response_data), status=200, content_type='application/json')
    else:
        # Return 404 if the short code is not found
        return web.Response(text="Short URL not found", status=404)
