#!/usr/bin/python3
"""
This script connects to a MySQL database and displays all values in the states table
of hbtn_0e_0_usa where the name matches the provided argument (safe from SQL injection).
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
