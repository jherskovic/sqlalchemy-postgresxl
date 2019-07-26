# setup.py
# Copyright (C) 2019 Jorge R. Herskovic <jherskovic@gmail.com>
# This work is based in part on the SQLAlchemy postgres dialect code written by the SQLAlchemy authors.
#
# Some parts are based on the Access adapter for SQLAlchemy by Mike Bayer, available at
# https://bitbucket.org/zzzeek/sqlalchemy-access/src/default/
# This module is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import os
import re

from setuptools import setup

v = open(os.path.join(os.path.dirname(__file__), 'sqlalchemy_postgresxl', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')


setup(name='sqlalchemy_postgresxl',
      version=VERSION,
      description="Postgresql-XL for SQLAlchemy",
      long_description=open(readme).read(),
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: CPython',
      'Topic :: Database :: Front-Ends',
      ],
      keywords='SQLAlchemy Postgres-XL',
      author='Jorge R. Herskovic',
      author_email='jherskovic@gmail.com',
      license='MIT',
      packages=['sqlalchemy_postgresxl'],
      include_package_data=True,
      tests_require=['nose >= 0.11'],
      test_suite="nose.collector",
      zip_safe=False,
      entry_points={
         'sqlalchemy.dialects': [
              'postgresxl = sqlalchemy_postgresxl.psycopg2:Pgxl_Dialect_psycopg2',
              'postgresxl.psycopg2 = sqlalchemy_postgresxl.psycopg2:Pgxl_Dialect_psycopg2',
              'postgresxl.psycopg2cffi = sqlalchemy_postgresxl.psycopg2cffi:Pgxl_Dialect_psycopg2cffi', # For PyPy
         ]
        }
)
