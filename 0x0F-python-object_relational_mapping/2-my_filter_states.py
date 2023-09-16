#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    port = 3306

    try:
        # Establish a connection to the MySQL database
        db = MySQLdb.connect(
            user=db_user,
            passwd=db_password,
            db=db_name,
            port=port
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Create the SQL query using the user input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
