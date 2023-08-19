#!/usr/bin/python3
"""lists all states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieving command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to the database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306,
        charset="utf8"
    )

    # Creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all the results from the query
    results = cursor.fetchall()

    # Printing the results
    for row in results:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
