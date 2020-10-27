import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="admin",
        password="admin.Fall2020.Fall2020",
        host="localhost",
        port=3306,
        database="Bus_Project"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()





# Getter Example
def testingTable_rows(testingTable_PK, name):
    cur.execute(
        "SELECT TestingTable_PK,Name FROM TestingTable",
        (testingTable_PK, name))