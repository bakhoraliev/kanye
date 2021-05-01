import requests as r


class InternalKanyeRestAPIError(Exception):
    ...


class KanyeRestAPIChangeError(Exception):
    ...


def quote() -> str:
    """Random Kanye West quote

    Raises:
        InternalKanyeRestAPIError: kanye.rest internal error
        KanyeRestAPIChangeError: kanye.rest API changed

    Returns:
        str: quote
    """
    try:
        response = r.get("https://api.kanye.rest/")
        response.raise_for_status()
    except Exception as exc:
        raise InternalKanyeRestAPIError(exc)

    try:
        return response.json()["quote"]
    except KeyError:
        raise KanyeRestAPIChangeError(response)


__all__ = ["quote"]
