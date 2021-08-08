#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
