import unittest
import os
from tempfile import mkdtemp
import shutil

from servertools import install_project, start_server

_project_root_dir = os.getcwd()

class TempDirTestCase(unittest.TestCase):
    def setUp(self):
        self.project_root_dir = _project_root_dir
        self.working_dir = mkdtemp('_chest')
       
    def tearDown(self):
        shutil.rmtree(self.working_dir)

class InstalledProjectTestCase(TempDirTestCase):
    def setUp(self):
        super(InstalledProjectTestCase, self).setUp()
        install_project(self.working_dir, self.project_root_dir)

    def tearDown(self):
        super(InstalledProjectTestCase, self).tearDown() 

class RunningServerTestCase(InstalledProjectTestCase):
    def setUp(self):
        super(RunningServerTestCase, self).setUp()
        self.server_process = start_server(self.working_dir)
        
    def tearDown(self):
        self.server_process.terminate()
        super(RunningServerTestCase, self).tearDown()
