#!/usr/bin/python3
"""Select stuff"""
import MySQLdb
import sys

args_list = sys.argv[1:]
HOST = '127.0.0.1'
USER = args_list[0]
PASS = args_list[1]
MY_DB = args_list[2]
if __name__ == '__main__':
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=MY_DB)
    cur = db.cursor()
    states = cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
