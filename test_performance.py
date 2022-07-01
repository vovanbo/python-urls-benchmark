#!/usr/bin/env python
import pytest

import furl
import hyperlink
import yarl
import urlobject

NON_ASCII_URL = 'http://εμπορικόσήμα.eu/путь/這裡'
NON_ASCII_URL_ENCODED = \
    'http://xn--jxagkqfkduily1i.eu/%D0%BF%D1%83%D1%82%D1%8C/%E9%80%99%E8%A3%A1'


@pytest.mark.benchmark(group='Creation of simple URL')
@pytest.mark.parametrize(
    'factory',
    [
        furl.furl,
        yarl.URL,
        urlobject.URLObject,
        hyperlink.URL.from_text
    ],
    ids=['furl', 'yarl', 'urlobject', 'hyperlink']
)
def test_create_simple_url(benchmark, factory):
    uri = 'http://example.com/path/to/?arg1=a&arg2=b#fragment'
    created_url = benchmark(factory, uri)
    if isinstance(created_url, furl.furl):
        assert created_url.url == uri
    elif isinstance(created_url, hyperlink.URL):
        assert created_url.to_uri().to_text() == uri
    else:
        assert str(created_url) == uri


@pytest.mark.benchmark(group='Creation of non-ASCII URL')
@pytest.mark.parametrize(
    'factory',
    [
        furl.furl,
        yarl.URL,
        urlobject.URLObject.from_iri,
        hyperlink.URL.from_text
    ],
    ids=['furl', 'yarl', 'urlobject', 'hyperlink']
)
def test_create_non_ascii_url(benchmark, factory):
    created_url = benchmark(factory, NON_ASCII_URL)
    if isinstance(created_url, furl.furl):
        assert created_url.url == NON_ASCII_URL_ENCODED
    elif isinstance(created_url, hyperlink.URL):
        assert created_url.to_uri().to_text() == NON_ASCII_URL_ENCODED
    else:
        assert str(created_url) == NON_ASCII_URL_ENCODED


@pytest.mark.benchmark(group='Conversion of URL to string')
@pytest.mark.parametrize(
    'created_url',
    [
        furl.furl(NON_ASCII_URL),
        yarl.URL(NON_ASCII_URL),
        urlobject.URLObject.from_iri(NON_ASCII_URL),
        hyperlink.URL.from_text(NON_ASCII_URL)
    ],
    ids=['furl', 'yarl', 'urlobject', 'hyperlink']
)
def test_url_to_string(benchmark, created_url):
    if isinstance(created_url, furl.furl):
        result = benchmark(created_url.tostr)
    elif isinstance(created_url, hyperlink.URL):
        result = benchmark(lambda: created_url.to_uri().to_text())
    else:
        result = benchmark(str, created_url)

    assert result == NON_ASCII_URL_ENCODED


if __name__ == '__main__':
    pytest.main(['--benchmark-histogram=benchmark', '--benchmark-min-time=1'])
