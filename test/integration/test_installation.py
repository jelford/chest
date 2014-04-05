#! /usr/bin/env python

from tempfile import mkdtemp
import os
import shutil
import subprocess

import unittest

_project_root_dir = os.getcwd()

def install_project(destination_directory, project_root_dir):
    subprocess.check_call(['virtualenv', destination_directory])
    installation_command = '. bin/activate; pip install {project_root_dir}'.format(**locals())
    subprocess.check_call(installation_command, shell=True, cwd=destination_directory)

class TestInstallation(unittest.TestCase):
    def setUp(self):
        self.project_root_dir = _project_root_dir
        self.working_dir = mkdtemp('_chest')

    def test_installation(self):
        install_project(self.working_dir, self.project_root_dir)
        
    def tearDown(self):
        shutil.rmtree(self.working_dir)

if __name__ == '__main__':
    unittest.main()
