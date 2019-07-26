from .base import PostgresXLDialect
from sqlalchemy.dialects.postgresql.psycopg2cffi import PGDialect_psycopg2cffi


class Pgxl_Dialect_psycopg2cffi(PostgresXLDialect, PGDialect_psycopg2cffi):
    pass

dialect = Pgxl_Dialect_psycopg2cffi

