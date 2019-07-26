from .base import PostgresXLDialect
from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2


class Pgxl_Dialect_psycopg2(PostgresXLDialect, PGDialect_psycopg2):
    pass

dialect = Pgxl_Dialect_psycopg2

