
from os import path
import subprocess

class Python(object):
    def __init__(self, virtual_env_directory):
        self.bin_dir = path.join(virtual_env_directory, 'bin')
        self.cwd = virtual_env_directory
        self.path = self.bin_dir

    def _run(self, python_args):
        return subprocess.Popen(['python'] + python_args, env={'PATH': self.path}, cwd=self.cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def start(self, script):
        return self._run([script])

    def start_module(self, module):
        return self._run(['-m', module])

if __name__ == '__main__':
    raise Exception()
