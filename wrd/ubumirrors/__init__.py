#!/usr/bin/env python
import urllib2
from BeautifulSoup import BeautifulSoup as BS
from httping import HTTPing

MIRROR_LIST='http://www.ubuntu.com/getubuntu/downloadmirrors'

extract_links = lambda x: x.findAll('a',{'class':'country_US continent_NA'})

def main():
    resp = urllib2.urlopen(MIRROR_LIST)
    page = BS(resp)
    for url in [link.attrMap['href'] for link in extract_links(page)]:
        hping = HTTPing(url, 2).ping()
        print url, hping

if __name__=="__main__":
    main()
