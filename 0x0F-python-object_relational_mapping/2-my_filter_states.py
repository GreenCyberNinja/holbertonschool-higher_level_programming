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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        state = row[1]
        if state == sys.argv[4]:
            print(row)

    cur.close()
    daba.close()


if __name__ == "__main__":
    getselect_states()
