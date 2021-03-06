#!/usr/bin/python3
"""DOCSTRING"""


import MySQLdb
import sys

if __name__ == '__main__':

    args_list = sys.argv[1:]
    USER = args_list[0]
    PASS = args_list[1]
    MY_DB = args_list[2]
    if len(args_list) > 4:
        NAME = args_list[3] + " " + args_list[4]
    else:
        NAME = args_list[3]
    db = MySQLdb.connect(user=USER, passwd=PASS, db=MY_DB)
    cur = db.cursor()
    states = cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
    ON states.id=cities.state_id WHERE states.name='{}' ORDER\
    BY cities.id".format(NAME))
    rows = cur.fetchall()
    if len(rows) == 1:
        print(rows[0][0])
    elif len(rows) > 1:
        print(rows[0][0], end="")
        for row in rows[1:]:
            print(", {}".format(row[0]), end="")
        print()
    else:
        print()
