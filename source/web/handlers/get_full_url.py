from aiohttp import web
from source.database.methods.read import get_original_url
from source.database.methods.update import increment_click_count


async def get_url(request: web.Request) -> web.Response:
    """
    Redirects the user to the original URL based on the provided short code.

    Args:
        request (web.Request): The incoming HTTP request containing 'short_code' in the URL.

    Returns:
        web.Response: Redirects to the original URL or returns an error if not found.
    """
    # Извлекаем short_code как строку из пути запроса
    short_code = request.match_info.get('short_code')

    if short_code is None:
        return web.Response(text="Short code is missing", status=400)

    # Получаем оригинальный URL из базы данных
    original_url = get_original_url(short_code)

    if original_url:
        # Увеличиваем счетчик кликов
        increment_click_count(short_code)
        # Перенаправляем на оригинальный URL
        return web.HTTPFound(location=original_url)
    else:
        # Возвращаем 404, если короткий код не найден
        return web.Response(text="Short URL not found", status=404)
