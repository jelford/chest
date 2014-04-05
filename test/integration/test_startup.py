#! /usr/bin/env python

import unittest
import test_installation
import subprocess
from subprocess import PIPE
#from subprocess import TimeoutExpired
import sys
import testtypes
from test_installation import install_project
from python_client import Python

def throw_if_fails_within(seconds, process):
    #try:
        from time import sleep
        sleep(seconds)
        ret_code = process.poll() #process.communicate(timout=seconds)
        if ret_code:
            stdout, stderr = process.communicate()
            raise Exception('failed to launch process')
        return process
    #except TimeoutExpired:
    #    return process

class TestStartup(testtypes.TempDirTestCase):
    def setUp(self):
        super(TestStartup, self).setUp()
        install_project(self.working_dir, self.project_root_dir)

    def test_can_start_up_once_installed(self):
        self.start_server(self.working_dir)
        subprocess.check_call('curl localhost:5805', shell=True)

    def start_server(self, base_dir):
        self.server_process = throw_if_fails_within(seconds=2, 
                process=Python(base_dir).start_module('chest.start'))

    def tearDown(self):
        self.server_process.terminate()
        super(TestStartup, self).tearDown()



if __name__ == '__main__':
    unittest.main()

