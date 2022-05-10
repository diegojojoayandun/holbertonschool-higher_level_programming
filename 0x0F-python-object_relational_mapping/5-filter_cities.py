#!/usr/bin/python3
"""
lists all  states  from the database  hbtn_0e_0_usa
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    _cursor = db.cursor()
    _cursor.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name=%s ORDER BY cities.id ASC", (argv[4], ))
    rows = _cursor.fetchall()

    _sep = ""
    for row in rows:
        print("{}{}".format(_sep, row[0]), end="")
        _sep = ", "
    print()

    _cursor.close()
    db.close()
