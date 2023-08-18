#!/usr/bin/python3
""" lists all cities of a given state from the hbtn_0e_4_usa database."""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""",  (state_name,))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
