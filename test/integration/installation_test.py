#! /usr/bin/env python

from tempfile import mkdtemp
import os
import shutil
import subprocess

def install_project(destination_directory, project_root_dir):
    subprocess.check_call(['virtualenv', destination_directory])
    installation_command = '. bin/activate; pip install {project_root_dir}'.format(**locals())
    subprocess.check_call(installation_command, shell=True, cwd=destination_directory)


if __name__ == '__main__':
    temp_dir = mkdtemp('_chest')
    try:
        project_root_directory = os.getcwd()
        install_project(temp_dir, project_root_directory)
    finally:
        shutil.rmtree(temp_dir)
