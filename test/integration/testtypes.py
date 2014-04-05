import unittest
import os
from tempfile import mkdtemp
import shutil

_project_root_dir = os.getcwd()

class TempDirTestCase(unittest.TestCase):
    def setUp(self):
        self.project_root_dir = _project_root_dir
        self.working_dir = mkdtemp('_chest')
       
    def tearDown(self):
        shutil.rmtree(self.working_dir)

