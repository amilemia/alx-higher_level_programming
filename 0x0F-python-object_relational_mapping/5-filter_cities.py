#!/usr/bin/python3
"""
Script that takes the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa (SQL injection safe).
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Check if all four required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".
              format(sys.argv[0]))
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

        # Create a parameterized SQL query to retrieve cities by state name
        query = (
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s ORDER BY cities.id ASC"
        )

        # Execute the query with the state_name as a parameter
        cursor.execute(query, (state_name,))

        # Fetch and print the results
        rows = cursor.fetchall()
        city_names = ', '.join(row[1] for row in rows)
        print(city_names)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
