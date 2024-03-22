#!/usr/bin/python3

"""
    This module lists all the cities from a state that's given
    as an argument, the results are sorted in ascending order
    using from hbtn_0e_0_usa database"""
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
    query = "SELECT cities.name\
                FROM cities INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name LIKE %s ORDER BY cities.id ASC"
    cur.execute(query, (f"{search}",))
    query_rows = cur.fetchall()
    for index, row in enumerate(query_rows):
        if index == len(query_rows) - 1:
            print(str(row).strip("('),"), end="")
        else:
            print(str(row).strip("('),"), end=", ")
    print()
    cur.close()
    conn.close()
