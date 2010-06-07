#!/usr/bin/env python

from datetime import datetime
import eventlet
from eventlet.green import httplib
from urlparse import urlparse
import operator

USER_AGENT='Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.2 Safari/533.4'

def http_connect(url,timeout=500):
    timeout=timeout/1000.0
    try:
        conn = httplib.HTTPConnection(url.netloc,
                port=url.port,
                timeout=timeout)
    except TypeError:
        return None

    try:
        stime = datetime.now()
        conn.request('HEAD', url.path, None, {'User-Agent': USER_AGENT})
        resp = conn.getresponse()
        etime = datetime.now()
        resp_code = resp.status
        resp_reason = resp.reason
    except Exception, e:
        return None
    finally:
        conn.close()

    if resp_code != 200:
        return None

    resp_time = (etime-stime).microseconds/1000
    return (resp_time, resp_code, resp_reason, resp.getheaders())

def http_ping_avg(url, count=3, timeout=500):
    url = urlparse(url)
    pool = eventlet.GreenPool()
    results = []
    for r in pool.imap(lambda x: http_connect(url, timeout), xrange(count)):
        if r:
            results.append(r[0])

    if not results:
        return None

    _sum = reduce(operator.add, results)
    _len = len(results)
    return float(_sum) / _len

if __name__=="__main__":
    print [x for x in http_ping_avg("wrd.nu")]

