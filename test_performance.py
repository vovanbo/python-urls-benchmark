#!/usr/bin/env python
import pytest

import furl
import yarl
import urlobject
from url import URL as URLPY

NON_ASCII_URL = 'http://εμπορικόσήμα.eu/путь/這裡'
NON_ASCII_URL_ENCODED = \
    'http://xn--jxagkqfkduily1i.eu/%D0%BF%D1%83%D1%82%D1%8C/%E9%80%99%E8%A3%A1'


@pytest.mark.benchmark(group='Creation of simple URL')
@pytest.mark.parametrize(
    'factory',
    [furl.furl, yarl.URL, urlobject.URLObject, URLPY.parse],
    ids=['furl', 'yarl', 'urlobject', 'url-py']
)
def test_create_simple_url(benchmark, factory):
    url = 'http://example.com/path/to/?arg1=a&arg2=b#fragment'
    created_url = benchmark(factory, url)
    if factory == URLPY.parse:
        assert str(created_url.punycode().escape()) == url
    elif factory == furl.furl:
        assert created_url.url == url
    else:
        assert str(created_url) == url


@pytest.mark.benchmark(group='Creation of non-ASCII URL')
@pytest.mark.parametrize(
    'factory',
    [furl.furl, yarl.URL, urlobject.URLObject.from_iri, URLPY.parse],
    ids=['furl', 'yarl', 'urlobject', 'url-py']
)
def test_create_non_ascii_url(benchmark, factory):
    created_url = benchmark(factory, NON_ASCII_URL)
    if factory == URLPY.parse:
        assert str(created_url.punycode().escape()) == NON_ASCII_URL_ENCODED
    elif factory == furl.furl:
        assert created_url.url == NON_ASCII_URL_ENCODED
    else:
        assert str(created_url) == NON_ASCII_URL_ENCODED


@pytest.mark.benchmark(group='Conversion of URL to string')
@pytest.mark.parametrize(
    'url',
    [furl.furl(NON_ASCII_URL),
     yarl.URL(NON_ASCII_URL),
     urlobject.URLObject.from_iri(NON_ASCII_URL),
     URLPY.parse(NON_ASCII_URL)],
    ids=['furl', 'yarl', 'urlobject', 'url-py']
)
def test_url_to_string(benchmark, url):
    if isinstance(url, URLPY):
        result = benchmark(lambda: url.punycode().escape())
    elif isinstance(url, furl.furl):
        result = benchmark(url.tostr)
    else:
        result = benchmark(str, url)

    assert result == NON_ASCII_URL_ENCODED


if __name__ == '__main__':
    pytest.main(['--benchmark-histogram=benchmark', '--benchmark-min-time=1'])
