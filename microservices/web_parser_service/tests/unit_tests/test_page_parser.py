from app.core.page_parser import PageParser


def test_parse(sample_html: str, parser: PageParser) -> None:
    parser = PageParser()
    title, links = parser.parse(sample_html, "http://example.com")

    assert title == "Test Page"
    assert links == [
        "http://example.com/page1",
        "http://example.com/page2"
    ]


def test_is_valid_url(parser: PageParser) -> None:
    http_url = "http://example.com"
    https_url = "https://example.com"
    ftp_url = "ftp://example.com"

    assert parser.is_valid_url(http_url) is True
    assert parser.is_valid_url(https_url) is True
    assert parser.is_valid_url(ftp_url) is False
