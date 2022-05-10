#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    _cursor = db.cursor()
    _cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' \
        ORDER BY states.id ASC".format(sys.argv[4]))
    rows = _cursor.fetchall()
    for row in rows:
        print(row)

    _cursor.close()
    db.close()
