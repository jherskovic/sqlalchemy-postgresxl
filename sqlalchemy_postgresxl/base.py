# sqlalchemy_postgresxl/base.py
# Copyright (C) 2019 Jorge R. Herskovic <jherskovic@gmail.com>
# This work is based in part on the SQLAlchemy postgres dialect code written by the SQLAlchemy authors.
#
# Some parts are based on the Access adapter for SQLAlchemy by Mike Bayer, available at
# https://bitbucket.org/zzzeek/sqlalchemy-access/src/default/
# This module is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from sqlalchemy.dialects.postgresql.base import *
from sqlalchemy.exc import NotSupportedError


class PostgresXLDDLCompiler(PGDDLCompiler):
    def post_create_table(self, table):
        pg_postcreate = super().post_create_table(table)
        pgxl_opts = table.dialect_options['postgresxl']
        pgxl_clauses = []

        if pgxl_opts['distribute_by']:
            distribution_kind = pgxl_opts['distribute_by']
            if distribution_kind.lower() not in ['hash', 'replication', 'roundrobin', 'modulo']:
                raise NotSupportedError("The specified distribute_by value (%s) is not supported." % distribution_kind)
            pgxl_clauses.append('\n DISTRIBUTE BY %s' % distribution_kind)

            if distribution_kind.lower() in ['hash', 'modulo']:
                if pgxl_opts['distribute_column']:
                    distribution_column = pgxl_opts['distribute_column']
                    pgxl_clauses.append(' (%s)' % distribution_column)
                else:
                    raise NotSupportedError("Use must specify a distribute_column when using hash or modulo distributions.")

        return pg_postcreate + "".join(pgxl_clauses)


class PostgresXLCompiler(PGCompiler):
    pass


class PostgresXLExecutionContext(PGExecutionContext):
    pass


class PostgresXLDialect(PGDialect):
    name = 'postgresxl'
    ddl_compiler = PostgresXLDDLCompiler
    statement_compiler = PostgresXLCompiler
    execution_ctx_cls = PostgresXLExecutionContext

    # Taken from PGDialect and augmented
    construct_arguments = [
        (
            schema.Index,
            {
                "using": False,
                "where": None,
                "ops": {},
                "concurrently": False,
                "with": {},
                "tablespace": None,
            },
        ),
        (
            schema.Table,
            {
                "ignore_search_path": False,
                "tablespace": None,
                "partition_by": None,
                "with_oids": None,
                "on_commit": None,
                "inherits": None,
                "distribute_by": None,
                "distribute_column": None,
            },
        ),
    ]
