#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
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

        new_state = State(name="California")
        new_state.cities = [City(name="San Francisco")]
        session.add(new_state)
        session.commit()

        session.close()

    except Exception as e:
        print("Error:", e)
