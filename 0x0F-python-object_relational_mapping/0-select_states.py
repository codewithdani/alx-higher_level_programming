#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states from the hbtn_0e_0_usa database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    res = c.fetchall()
    for data in res:
        print(data)
    c.close()
    db.close()
