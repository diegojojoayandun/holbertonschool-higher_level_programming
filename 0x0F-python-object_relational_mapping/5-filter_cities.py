#!/usr/bin/env python3
""" lists all  states  from the database  hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    _cursor = db.cursor()
    _cursor.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = _cursor.fetchall()

    for row in rows:
        print(row)
