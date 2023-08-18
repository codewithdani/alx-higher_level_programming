#!/usr/bin/python3
""" This script connects to a MySQL database and lists all states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    res = cur.fetchall()
    for r in res:
        print(r)
    cur.close()
    db.close()
