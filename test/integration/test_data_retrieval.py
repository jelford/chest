#! /usr/bin/env python

import unittest

from testtypes import RunningServerTestCase
from servertools import HttpRequestMaker

class StoreAndRetrieveDataTestCase(RunningServerTestCase, HttpRequestMaker):
    def test_can_stash_data(self):
        self.assertEqual(self.post('series_name', {'value': 10}).status_code, 200)
        r = self.get('series_name')
        self.assertEqual(r.status_code, 200)
        data_returned = r.json()
        self.assertTrue(u'd' in data_returned)
        points = data_returned[u'd']
        self.assertEqual(len(points), 1)    
        self.assertEqual(points[0][u'value'], 10)

if __name__ == '__main__':
    unittest.main()
