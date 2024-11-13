from sqlalchemy.exc import NoResultFound
from source.database.main import Database
from source.database.models.short_url import ShortURL

def delete_short_url(short_code: str) -> bool:
    """
    Deletes a shortened URL from the database by short code.

    Args:
        short_code (str): The short code for the shortened URL.

    Returns:
        bool: True if the shortened URL was found and deleted successfully, False if not found.

    This function deletes the entry based on the provided short code.
    """
    session = Database().session

    try:
        # Locate the short URL by short code
        url_entry = session.query(ShortURL).filter(ShortURL.short_code == short_code).one()
        session.delete(url_entry)
        session.commit()
        return True

    except NoResultFound:
        return False

    finally:
        session.close()
