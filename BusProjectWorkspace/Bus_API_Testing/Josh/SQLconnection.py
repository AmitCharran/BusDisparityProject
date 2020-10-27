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


# Setter Example (Adding one row)
def add_testingTable_Row(testingTable_PK, name):
   
   cur.execute("INSERT INTO TestingTable(TestingTable_PK, Name) VALUES (?, ?)",
      (testingTable_PK, name))

# Getter Example
def testingTable_rows():
    cur.execute(
        "SELECT TestingTable_PK,Name FROM TestingTable"
        )
    return cur

# Using the Setter Function
add_testingTable_Row(100, "josh")




# Using the Getter Function
retrieve = testingTable_rows()
for(TestingTable_PK, Name) in retrieve:
    print(f"TestingTable_PK: {TestingTable_PK}, Name: {Name}")


# use commit() to commit to the database
#conn.commit()


# Closing connection after used
conn.close()