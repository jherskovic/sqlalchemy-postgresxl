SQLAlchemy-postgresxl
=====================

Jorge R. Herskovic <jherskovic@gmail.com>

A Postgres-XL SQLAlchemy dialect (inherits its functionality from the built-in Postgres dialect,
so postgres applications should work out of the box)

It accepts two different drivers:

- ``psycopg2``
- ``psycopg2cffi``

and it adds two table-level options:

- ``postgresxl_distribute_by``: ``[hash|modulo|replication|roundrobin]``
- ``postgresxl_distribute_column``: [name of the column to hash or modulo on; required for those two distribution modes]

``postgresxl_distribute_column`` is ignored if the ``distribute_by`` option is ``replication`` or ``roundrobin``.

That's pretty much it.

Example, using declarative:

::

    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class SomeClass(Base):
        __tablename__ = 'some_table'
        __table_args__ = {
            'postgresxl_distribute_by': 'hash',
            'postgresxl_distribute_column': 'id',
        }
        id = Column(Integer, primary_key=True)
        name =  Column(String(50))


    class SomeClass2(Base):
        __tablename__ = 'some_other_table'
        __table_args__ = {
            'postgresxl_distribute_by': 'replication',
        }
        id = Column(Integer, primary_key=True)
        name =  Column(String(50))

