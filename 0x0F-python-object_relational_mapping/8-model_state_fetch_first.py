#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

        Session = sessionmaker(bind=engine)
        session = Session()

        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        session.close()

    except Exception as e:
        print("Error:", e)
