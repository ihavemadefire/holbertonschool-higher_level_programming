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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
