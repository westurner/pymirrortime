#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup as BS
from httping import http_ping_avg
from itertools import ifilter
import eventlet
import random

MIRROR_LIST='http://www.ubuntu.com/getubuntu/downloadmirrors'
LOCATION_CLASSES="country_US continent_NA"

extract_links = lambda x: x.findAll('a',{'class':LOCATION_CLASSES})

def ping_url(url):
    ping_avg = http_ping_avg(url)
    if not ping_avg:
        print "  --- : %s" % (url)
        return None
    else:
        print "%5.d : %s" % (ping_avg, url)
        return (ping_avg,url)

def main():

    # Get the list of links
    resp = urllib2.urlopen(MIRROR_LIST)
    page = BS(resp)
    links = [link.attrMap['href'] for link in extract_links(page)]

    # Mix it up
    random.seed()
    random.shuffle(links)

    pool = eventlet.GreenPool()
    results = []
    for r in pool.imap(ping_url, links):
        results.append(r)

    fastest=min(ifilter(bool,results))

    print "-------- Fastest ----------"
    print "%5.d : %s" % (fastest[0], fastest[1])

if __name__=="__main__":
    main()
