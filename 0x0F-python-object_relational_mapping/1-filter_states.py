#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=db_user,
        passwd=db_password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
