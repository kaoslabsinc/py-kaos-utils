from collections.abc import Generator

from .typing import T


def paginate_generator(generator: Generator[T, None, None], limit: int) -> Generator[list[T], None, None]:
    """
    If limit is zero (or negative for that matter), it returns the whole generator as a list
    """
    page: list[T] = []
    for item in generator:
        page.append(item)
        if len(page) == limit:
            yield page
            page = []
    if page:  # Last page
        yield page
