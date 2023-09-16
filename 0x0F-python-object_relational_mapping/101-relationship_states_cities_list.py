#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db_user, db_password, db_name = sys.argv[1:4]

    try:
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(db_user, db_password, db_name),
            pool_pre_ping=True,
        )

        Base.metadata.create_all(engine)  # Create tables

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).order_by(State.id).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))

        session.close()

    except Exception as e:
        print("Error:", e)
