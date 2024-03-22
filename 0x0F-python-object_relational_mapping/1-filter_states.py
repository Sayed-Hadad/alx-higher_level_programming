#!/usr/bin/python3

"""This module lists all the states that starts with N
    sorted in ascending order from hbtn_0e_0_usa database"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    usr = argv[1]
    password = argv[2]
    db_name = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=usr, passwd=password, db=db_name,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%'\
              ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
