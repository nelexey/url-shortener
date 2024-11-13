from typing import Dict, List

from .handlers.make_short_url import make_short_url
from .handlers.get_full_url import get_url
from .handlers.get_url_stats import get_stats
from .handlers.delete_short_url import delete_url

# Define URL route configurations for the web server
urls: List[Dict[str, str]] = [
    {
        'method': 'POST',
        'path': '/shorten',             # URL path for creating a new short URL
        'handler': make_short_url           # Function to handle POST requests for URL shortening
    },
    {
        'method': 'GET',
        'path': '/stats/{short_code}',  # URL path for retrieving URL statistics
        'handler': get_stats            # Function to handle GET requests for stats
    },
    {
        'method': 'GET',
        'path': '/delete/{short_code}', # URL path for deleting a short URL
        'handler': delete_url         # Function to handle DELETE requests for URL deletion
    },
    {
        'method': 'GET',
        'path': '/{short_code}', # URL path for redirecting to the original URL
        'handler': get_url         # Function to handle GET requests for redirection
    },
]
