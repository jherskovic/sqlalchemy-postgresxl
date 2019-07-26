# sqlalchemy_postgresxl/__init__.py
# Copyright (C) 2019 Jorge R. Herskovic <jherskovic@gmail.com>
# This work is based in part on the SQLAlchemy postgres dialect code written by the SQLAlchemy authors.
#
# Some parts are based on the Access adapter for SQLAlchemy by Mike Bayer, available at
# https://bitbucket.org/zzzeek/sqlalchemy-access/src/default/
# This module is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

__version__ = '0.1'

from sqlalchemy.dialects import registry
from . import psycopg2

base.dialect = dialect = psycopg2.dialect

registry.register("postgresxl", "sqlalchemy_postgresxl.psycopg2", "Pgxl_Dialect_psycopg2")
registry.register("postgresxl.psycopg2", "sqlalchemy_postgresxl.psycopg2", "Pgxl_Dialect_psycopg2")
registry.register("postgresxl.psycopg2cffi", "sqlalchemy_postgresxl.psycopg2cffi", "Pgxl_Dialect_psycopg2cffi")