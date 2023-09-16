#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
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

        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
        else:
            print("Not found")

        session.close()

    except Exception as e:
        print("Error:", e)
