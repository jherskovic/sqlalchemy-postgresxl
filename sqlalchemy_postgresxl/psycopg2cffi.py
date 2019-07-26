# sqlalchemy_postgresxl/psycopg2cffi.py
# Copyright (C) 2019 Jorge R. Herskovic <jherskovic@gmail.com>
# This work is based in part on the SQLAlchemy postgres dialect code written by the SQLAlchemy authors.
#
# Some parts are based on the Access adapter for SQLAlchemy by Mike Bayer, available at
# https://bitbucket.org/zzzeek/sqlalchemy-access/src/default/
# This module is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from .base import PostgresXLDialect
from sqlalchemy.dialects.postgresql.psycopg2cffi import PGDialect_psycopg2cffi


class Pgxl_Dialect_psycopg2cffi(PostgresXLDialect, PGDialect_psycopg2cffi):
    pass

dialect = Pgxl_Dialect_psycopg2cffi

