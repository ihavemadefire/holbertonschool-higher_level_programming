#!/usr/bin/python3
"""This module does awesome stuff"""
import MySQLdb
import sys

if __name__ == '__main__':

    args_list = sys.argv[1:]
    USER = args_list[0]
    PASS = args_list[1]
    MY_DB = args_list[2]
    INPUT = args_list[3]

    db = MySQLdb.connect(user=USER, passwd=PASS, db=MY_DB)
    cur = db.cursor()
    states = cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id".
                         format(INPUT))
    rows = cur.fetchall()
    for row in rows:
        print(row)
