#!/usr/bin/python3
# script to list all states from database hbtn_0e_0_usa
from sys import argv as av
""" script to connect to db and access info """
import MySQLdb


if __name__ == "__main__":
    ac = len(av)
    if ac < 4:
        exit()
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=av[1],
                           passwd=av[2],
                           db=av[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
