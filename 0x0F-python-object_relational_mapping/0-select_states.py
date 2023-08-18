#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states from the hbtn_0e_0_usa database.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = "root"
    password = "root"
    database = "my_db"

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()

    # Execute the SQL query to select all states and order by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
