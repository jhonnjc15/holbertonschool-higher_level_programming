#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM cities\
                INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id")
    print(", ".join([cities[2] for cities in c.fetchall()
                    if cities[4] == sys.argv[4]]))
    c.close()
    db.close()
