from sqlalchemy.exc import NoResultFound
from source.database.main import Database
from source.database.models.short_url import ShortURL

def increment_click_count(short_code: str) -> bool:
    """
    Increments the click count for a shortened URL in the database.

    Args:
        short_code (str): The short code for the shortened URL.

    Returns:
        bool: True if the click count was incremented successfully, False if the short code was not found.

    This function increases the click count each time the short URL is accessed.
    """
    session = Database().session

    try:
        # Locate the short URL by short code
        url_entry = session.query(ShortURL).filter(ShortURL.short_code == short_code).one()
        url_entry.clicks += 1  # Increment click count
        session.commit()
        return True

    except NoResultFound:
        return False

    finally:
        session.close()
