#! /usr/bin/env python

import unittest

from testtypes import RunningServerTestCase
from servertools import HttpRequestMaker

class StoreAndRetrieveDataTestCase(RunningServerTestCase, HttpRequestMaker):
    def test_can_stash_data(self):
        self.assertEqual(self.post('series_name', {'value': 10}).status_code, 200)
        r = self.get('series_name')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {u'd': [ {'value': 10} ] })


if __name__ == '__main__':
    unittest.main()
