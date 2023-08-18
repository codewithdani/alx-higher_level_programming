#!/usr/bin/python3
""" lists all cities from the hbtn_0e_4_usa database."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database,
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON states.id=cities.state_id""")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
