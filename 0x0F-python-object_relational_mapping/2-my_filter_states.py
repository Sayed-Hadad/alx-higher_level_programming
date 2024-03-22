#!/usr/bin/python3

"""
    This module lists all rows that contains a value given
    as an argument, results are sorted in ascending order
    from hbtn_0e_0_usa database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    usr = argv[1]
    password = argv[2]
    db_name = argv[3]
    search = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=usr, passwd=password, db=db_name,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY'{}' \
            ORDER BY states.id ASC".format(search))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
