#! /usr/bin/env python

from subprocess import check_call

import testtypes
from servertools import start_server, install_project

class TestStartup(testtypes.InstalledProjectTestCase):
    def setUp(self):
        super(TestStartup, self).setUp()

    def test_can_start_up_once_installed(self):
        self.start_server(self.working_dir)
        check_call('curl localhost:5805', shell=True)

    def start_server(self, base_dir):
        self.server_process = start_server(base_dir)

    def tearDown(self):
        self.server_process.terminate()
        super(TestStartup, self).tearDown()

if __name__ == '__main__':
    import unittest
    unittest.main()

