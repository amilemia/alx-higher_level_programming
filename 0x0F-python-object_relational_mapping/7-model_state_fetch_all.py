#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if all three required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Create an SQLAlchemy engine to connect to the MySQL database
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(db_user, db_password, db_name),
            pool_pre_ping=True,
        )

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and retrieve all State objects sorted by id
        states = session.query(State).order_by(State.id).all()

        # Print the results
        for state in states:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        if session:
            session.close()
