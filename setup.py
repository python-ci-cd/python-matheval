#!/usr/bin/env python

from setuptools import setup

setup(name='matheval',
      version='1.0',
      description='Evaluation of expression trees',
      author='Moritz Lenz',
      author_email='moritz.lenz@gmail.com',
      url='https://deploybook.com/',
      package_dir={'': 'src'},
      requires=['flask', 'nose'],
      test_suite='nose.collector',
      packages=['matheval']
     )
