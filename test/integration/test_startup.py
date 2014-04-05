#! /usr/bin/env python

import unittest
import test_installation
import subprocess
from subprocess import PIPE
#from subprocess import TimeoutExpired
import sys

def throw_if_process_fails_within(seconds, process):
    #try:
        from time import sleep
        sleep(seconds)
        ret_code = process.poll() #process.communicate(timout=seconds)
        if ret_code:
            raise Exception('failed to launch process')
    #except TimeoutExpired:
    #    return process

def start_server(base_dir):
    server_process = subprocess.Popen('. bin/activate; python -m chest.start', 
            shell=True, cwd=base_dir, stdout=sys.stdout, stderr=sys.stderr)
    throw_if_process_fails_within(2, server_process)
    return server_process

class TestStartup(test_installation.TestInstallation):
    def test_can_start_up_once_installed(self):
        self.test_installation()
        server_process = start_server(self.working_dir)
        subprocess.check_call('curl localhost:5805', shell=True)

if __name__ == '__main__':
    unittest.main()

