from typing import Optional
from sqlalchemy.exc import NoResultFound
from source.database.main import Database
from source.database.models.short_url import ShortURL

def get_original_url(short_code: str) -> Optional[str]:
    """
    Retrieves the original URL by its short code from the database.

    Args:
        short_code (str): The short code for the shortened URL.

    Returns:
        Optional[str]: The original URL if found; otherwise, None.

    This function retrieves the original URL based on the provided short code.
    """
    session = Database().session
    try:
        # Query for original URL by short code
        url_entry = session.query(ShortURL).filter(ShortURL.short_code == short_code).one()
        return url_entry.original_url

    except NoResultFound:
        return None

    finally:
        session.close()

def get_url_stats(short_code: str) -> Optional[ShortURL]:
    """
    Retrieves statistics for the specified short URL.

    Args:
        short_code (str): The unique short code for the URL.

    Returns:
        Optional[ShortURL]: The ShortURL object containing the stats if found; otherwise, None.
    """
    session = Database().session

    try:
        # Query for the short URL stats by short_code
        url_data = session.query(ShortURL).filter(ShortURL.short_code == short_code).one()
        return url_data

    except NoResultFound:
        # Return None if no record is found
        return None

    finally:
        session.close()