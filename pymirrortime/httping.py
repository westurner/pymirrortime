#!/usr/bin/env python
from __future__ import print_function
import operator
from datetime import datetime
from urlparse import urlparse

import eventlet
from eventlet.green import httplib
from functools import reduce

USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.2 Safari/533.4'


import collections

HTTPResult = collections.namedtuple('HTTPResult',
                                    ('time', 'code', 'reason', 'headers',
                                     'start', 'end'))


def _parse_url(url):
    if not hasattr(url, 'netloc'):
        if not url.startswith('http'):
            url = 'http://%s/' % url
        url = urlparse(url)
    return url


def http_connect(url, timeout=500):
    """
    Time a request to an HTTP server.

    Args:
        url (str or urlparse.ParseResult): -- URL to connect to
        timeout (int) -- connection timeout

    Returns:
        (resp_time, resp_code, resp_reason, resp.getheaders())

    """
    timeout = timeout / 1000.0
    url = _parse_url(url)

    try:
        conn = httplib.HTTPConnection(url.netloc,
                                      port=url.port,
                                      timeout=timeout)

        stime = datetime.now()
        conn.request('HEAD', url.path, None, {'User-Agent': USER_AGENT})
        resp = conn.getresponse()
        etime = datetime.now()
        resp_code = resp.status
        resp_reason = resp.reason
    except Exception:  # as e:
        raise
        # return None
    finally:
        conn.close()

    if resp_code != 200:
        return None

    resp_time = (etime-stime).microseconds / 1000
    return HTTPResult(resp_time, resp_code, resp_reason, resp.getheaders(),
                      stime, etime)


def http_ping_avg(url, count=3, timeout=5000):
    """
    Return the regular average of count HTTP connections to url.

    Args:
        url (str or urlparse.ParseResult): URL to connect to
        count (int): number of connections to make
        timeout (int): connection timeout

    Returns:
        float: mean of connection timings

    """
    url = _parse_url(url)
    pool = eventlet.GreenPool()
    results = []
    for r in pool.imap(lambda x: http_connect(url, timeout), xrange(count)):
        if r:
            results.append(r.time)

    if not results:
        return None

    _sum = reduce(operator.add, results)
    _len = len(results)
    return float(_sum) / _len


def main(*args):
    import sys
    hostname = "localhost"
    if len(sys.argv) == 2:
        hostname = sys.argv[1]
    elif len(sys.argv) >= 2:
        raise Exception(sys.argv)

    results = http_ping_avg(hostname)
    if results is not None:
        print(results)
    else:
        raise Exception('no results?')

if __name__ == "__main__":
    import sys
    main(*sys.argv)
