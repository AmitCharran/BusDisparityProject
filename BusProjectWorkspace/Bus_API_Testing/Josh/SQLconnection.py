import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="admin",
        password="",
        host="localhost",
        port=3306,
        database="Bus_Project"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()