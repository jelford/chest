#! /usr/bin/env python

import unittest
import requests
import json

from testtypes import RunningServerTestCase

class StoreAndRetrieveDataTestCase(RunningServerTestCase):
    def post(self, path, data):
        r = requests.post('http://localhost:5805/{path}'.format(path=path), data=json.dumps(data))
        self.assertEqual(r.status_code, 200)
        return r

    def get(self, path):
        r = requests.get('http://localhost:5805/{path}'.format(path=path))
        self.assertEqual(r.status_code, 200)
        return r

    def test_can_stash_data(self):
        self.post('series_name', {'value': 10})
        r = self.get('series_name')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {u'd': [ {'value': 10} ] })


if __name__ == '__main__':
    unittest.main()
