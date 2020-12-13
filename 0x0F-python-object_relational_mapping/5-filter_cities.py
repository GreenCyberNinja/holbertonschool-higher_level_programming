#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys


def getselect_states():
    """requires usr password and table returns all states"""
    daba = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = daba.cursor()
    cmd = "SELECT  cities.name FROM states\
           INNER JOIN cities ON states.id = cities.state_id\
           WHERE states.name LIKE %s\
           ORDER BY cities.id ASC;"
    cur.execute(cmd, (sys.argv[4],))
    query_rows = cur.fetchall()
    sp
    for row in query_rows:
        print(sp, end="")
        print(row[0], end="")
        sep = ", "
    print()
    cur.close()
    daba.close()


if __name__ == "__main__":
    getselect_states()
