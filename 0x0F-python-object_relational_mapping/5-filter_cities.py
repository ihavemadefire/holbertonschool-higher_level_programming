#!/usr/bin/python3
import MySQLdb
import sys

args_list = sys.argv[1:]
HOST = '127.0.0.1'
USER = args_list[0]
PASS= args_list[1]
MY_DB = args_list[2]
NAME = args_list[3]

if __name__ =='__main__':
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=MY_DB)
    cur = db.cursor()
    states = cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON states.id = cities.state_id WHERE states.name ='{}'  ORDER BY cities.id".format(NAME))
    rows = cur.fetchall()
    print (rows[0][0], end=" ")
    for row in rows[1:]:
        print (", {}".format(row[0]), end="")
    print ()
    cur.close()
    db.close()
