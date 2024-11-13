from sqlalchemy.exc import NoResultFound
from source.database.main import Database
from source.database.models.short_url import ShortURL


def create_short_url(original_url: str, short_code: str) -> None:
    """
    Adds a new shortened URL to the database if the short code does not already exist.

    Args:
        original_url (str): The original URL to be shortened.
        short_code (str): Unique short code for the shortened URL.

    This function adds a new entry in the database for the shortened URL.
    """
    session = Database().session

    try:
        # Attempt to find an existing short code
        session.query(ShortURL).filter(ShortURL.short_code == short_code).one()

    except NoResultFound:
        # If short code does not exist, create a new entry
        new_short_url = ShortURL(
            original_url=original_url,
            short_code=short_code,
        )
        session.add(new_short_url)
        session.commit()

    finally:
        session.close()
