import pytest
import httpretty
import kanye


@httpretty.activate
def test_quote_must_be_returned():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.kanye.rest",
        '{"quote":"Cool Kanye West quote"}',
    )
    assert kanye.quote() == "Cool Kanye West quote"


@httpretty.activate
def test_quote_with_bad_http_status():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.kanye.rest",
        "Internal server error",
        status=500,
    )
    with pytest.raises(kanye.InternalKanyeRestAPIError):
        kanye.quote()


@httpretty.activate
def test_quote_with_bad_response():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.kanye.rest",
        '{"cool_quote": "Kanye West cool quote"}',
    )
    with pytest.raises(kanye.KanyeRestAPIChangeError):
        kanye.quote()
