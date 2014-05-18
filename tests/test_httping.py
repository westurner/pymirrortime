import unittest

from pymirrortime.httping import http_connect, http_ping_avg, _parse_url
from pymirrortime.httping import HTTPResult


class test___parse_url(unittest.TestCase):

    def test__parse_url(self):
        IO = [
            ('localhost', 'localhost'),
            ('localhost:80', 'localhost:80'),
            ('localhost:443', 'localhost:443'),
            ('http://localhost', 'localhost'),
        ]
        for i, expected_o in IO:
            print(i)
            loc = _parse_url(i)
            self.assertEqual(loc.netloc, expected_o)


class Test__http_connect(unittest.TestCase):

    def test_http_connect(self):
        I = [('localhost',), ]
        for i in I:
            o = http_connect(*i)
            self.assertIsInstance(o, HTTPResult)
            self.assertEqual(o.code, 200)


class Test__http_ping_avg(unittest.TestCase):

    def test_http_ping_avg(self):
        I = [('localhost',), ]
        for i in I:
            o = http_ping_avg(*i)
            print(o)
            self.assertIsInstance(o, float)
