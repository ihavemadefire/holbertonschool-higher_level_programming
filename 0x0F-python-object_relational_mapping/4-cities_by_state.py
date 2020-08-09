#!/usr/bin/python3
"""DOCSTRING"""

import MySQLdb
import sys

if __name__ == '__main__':
    args_list = sys.argv[1:]
    USER = args_list[0]
    PASS = args_list[1]
    MY_DB = args_list[2]
    db = MySQLdb.connect(user=USER, passwd=PASS, db=MY_DB)
    cur = db.cursor()
    states = cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
