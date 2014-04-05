#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="chest",
    version="0.1.0_0",

    author='James Elford',
    author_email='james.p.elford@gmail.com',
    description='A web service for storing and serving arbitrary data series',
    license='BSD 3-clause',

    packages=find_packages("src"),
    package_dir={'': 'src'},
    package_data={'': ['*.html']},
    install_requires = [
        'tornado>=3.2',
    ],

    test_suite = 'test.integration',

    tests_require = [
        'requests>=2.2'
    ]
    
)
