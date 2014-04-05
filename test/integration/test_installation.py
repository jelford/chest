#! /usr/bin/env python

from tempfile import mkdtemp
import os
import shutil
import subprocess

import unittest
import testtypes

from servertools import install_project

class TestInstallation(testtypes.TempDirTestCase):
    def test_installation(self):
        install_project(self.working_dir, self.project_root_dir)
        
if __name__ == '__main__':
    unittest.main()
