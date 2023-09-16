#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Check if all three required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Establish a connection to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user=db_user,
            passwd=db_password,
            db=db_name,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute SQL query to retrieve all cities and their respective states
        cursor.execute(
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
