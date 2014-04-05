#! /usr/bin/env python

import unittest

from testtypes import RunningServerTestCase
from servertools import HttpRequestMaker

class RetrieveCharHtmlTestCase(RunningServerTestCase, HttpRequestMaker):
    def test_unknown_chart_returns_404(self):
        r = self.get('unknown_data_series/chart')
        self.assertEqual(r.status_code, 404)
       
    def test_known_data_chart_returns_html(self):
        self.post('known_series', data={'v': 1})
        r = self.get('known_series/chart')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('text/html' in r.headers['content-type'])

if __name__ == '__main__':
    unittest.main()
