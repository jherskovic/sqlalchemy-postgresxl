__version__ = '0.1'

from sqlalchemy.dialects import registry
from . import psycopg2

base.dialect = dialect = psycopg2.dialect

registry.register("postgresxl", "sqlalchemy_postgresxl.psycopg2", "Pgxl_Dialect_psycopg2")
registry.register("postgresxl.psycopg2", "sqlalchemy_postgresxl.psycopg2", "Pgxl_Dialect_psycopg2")
registry.register("postgresxl.psycopg2cffi", "sqlalchemy_postgresxl.psycopg2cffi", "Pgxl_Dialect_psycopg2cffi")