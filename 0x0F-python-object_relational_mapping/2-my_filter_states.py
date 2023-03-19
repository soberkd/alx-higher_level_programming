#!/usr/bin/python3
"""  this script takes in an argument and displays all values
     in the states table of hbtn_0e_0_usa where name
     matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name, search = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{}'ORDER BY id ASC"
    cur.execute(query.format(search))
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    conn.close()
