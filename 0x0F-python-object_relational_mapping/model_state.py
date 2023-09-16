#!/usr/bin/python3
"""
This script creates a State class and links it to a MySQL table.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class with SQLAlchemy mapping to the states table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".
            format(db_user, db_password, db_name),
            pool_pre_ping=True,
        )
        Base.metadata.create_all(engine)

    except Exception as e:
        print("Error:", e)
