import json
import hashlib
import time
from aiohttp import web
from typing import Dict

from source.database.methods.create import create_short_url


def generate_short_code(url: str) -> str:
    """
    Generates a short code based on URL content and timestamp.
    Returns 6-character string using URL-safe characters.
    """
    # Combine URL with timestamp for uniqueness
    timestamp = str(int(time.time()))
    input_string = f"{url}{timestamp}".encode('utf-8')

    # Generate hash and take first 6 characters
    hash_object = hashlib.md5(input_string)
    hash_hex = hash_object.hexdigest()

    # Convert to URL-safe string:
    # - Take first 6 characters of hash
    # - Ensure we use URL-safe characters by replacing unsafe ones
    safe_chars = {
        'a': 'G', 'b': 'H', 'c': 'J', 'd': 'K', 'e': 'M', 'f': 'N',
        '0': 'P', '1': 'Q', '2': 'R', '3': 'S', '4': 'T',
        '5': 'W', '6': 'X', '7': 'Y', '8': 'Z', '9': 'V'
    }

    short_code = ""
    for char in hash_hex[:6]:
        short_code += safe_chars.get(char, char.upper())

    return short_code


async def make_short_url(request: web.Request) -> web.Response:
    """
    Handles the incoming HTTP request to create a shortened URL, parses the JSON data,
    validates the required 'original_url' parameter, generates a unique short code,
    and returns an appropriate response.

    Args:
        request (web.Request): The incoming HTTP request containing JSON data.

    Returns:
        web.Response: The HTTP response with the short code or an error message.
    """
    try:
        # Parse JSON data from the request
        data: Dict = await request.json()
    except json.JSONDecodeError:
        return web.Response(text="Invalid JSON data", status=400)

    # Retrieve and validate 'original_url' from the parsed data
    original_url = data.get('original_url')
    if not original_url:
        return web.Response(text="Missing 'original_url' parameter", status=400)

    # Validate URL format
    if not original_url.startswith(('http://', 'https://')):
        return web.Response(text="Invalid URL format. Must start with http:// or https://", status=400)

    try:
        # Generate short code based on URL content
        short_code = generate_short_code(original_url)

        # Create the short URL in the database using existing method
        create_short_url(original_url=original_url, short_code=short_code)

        # Prepare and return the success response
        response_data = {"short_code": short_code}
        return web.Response(
            text=json.dumps(response_data),
            status=201,
            content_type='application/json'
        )

    except Exception as e:
        return web.Response(text=f"Error creating short URL: {str(e)}", status=500)