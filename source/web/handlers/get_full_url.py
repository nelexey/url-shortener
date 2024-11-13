from aiohttp import web
from source.database.methods.read import get_original_url
from source.database.methods.update import increment_click_count

async def get_url(request: web.Request) -> web.Response:
    """
    Handles a request to retrieve and redirect to the original URL using a short code.

    This function extracts the 'short_code' from the incoming request path,
    retrieves the corresponding original URL from the database, and redirects
    the user to that URL. If the short code is invalid or not found, it returns
    an appropriate error response.

    Args:
        request (web.Request): The incoming HTTP request containing 'short_code' in the URL.

    Returns:
        web.Response: A redirection to the original URL or an error response if the short code is invalid or not found.
    """
    # Extract 'short_code' from the request URL path
    short_code: str = request.match_info.get('short_code', "")

    if not short_code:
        return web.Response(text="Short code is missing", status=400)

    # Retrieve the original URL from the database
    original_url = get_original_url(short_code)

    if original_url:
        # Increment click count for the short code
        increment_click_count(short_code)
        # Redirect to the original URL
        return web.HTTPFound(location=original_url)
    else:
        # Return 404 if the short code is not found
        return web.Response(text="Short URL not found", status=404)
