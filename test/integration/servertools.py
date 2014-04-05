
import subprocess
from python_client import Python
import requests
import json

def install_project(destination_directory, project_root_dir):
    subprocess.check_call(['virtualenv', destination_directory])
    installation_command = '. bin/activate; pip install {project_root_dir}'.format(**locals())
    subprocess.check_call(installation_command, shell=True, cwd=destination_directory)


def _throw_if_fails_within(seconds, process):
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

def start_server(base_dir):
    return _throw_if_fails_within(seconds=2, 
                process=Python(base_dir).start_module('chest.start'))

class HttpRequestMaker(object):
    def post(self, path, data):
        r = requests.post('http://localhost:5805/' + path, data=json.dumps(data))
        return r

    def get(self, path):
        r = requests.get('http://localhost:5805/' + path)
        return r
