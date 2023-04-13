import sqlite3

# in case you dont have a database this will automatically create one
conn = sqlite3.connect("./database/alpha.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS people
                (first_name TEXT, last_name TEXT)''') 

conn.commit()
cur.close()

# execute simple query
cur = conn.cursor()
cur.execute('''INSERT INTO people (first_name, last_name)
                VALUES ("John", "Heart")''') 
conn.commit()
cur.close()           

# --

names_list = [
        ("Rod", "Watson"),
        ("Roger", "Homes"),
        ("Petri", "Hawtorn"),
        ("Jus", ""),
        ("James", "McCann")
]

# execute multiple queries usign placeholders for safeguard
cur = conn.cursor()
cur.executemany('''INSERT INTO people (first_name, last_name)
                   VALUES (?, ?)''', names_list)
conn.commit()
cur.close()           

# --

# execute a entire script, acn be a file or a string
cur = conn.cursor()

with open("script.sql") as file:
        sql_script = file.read()

cur.executescript(sql_script)

# --

cur = conn.cursor()

# When you execute a query usign a cursor, it returns a cursor
# You can iterate over the cursor itself. But for good pratices just store in another variable
people_data = cur.execute("SELECT * FROM people ORDER BY first_name")
for row in people_data:
        print(row)

# --

# always remember to close connection and cursors as security maner to avoid sql injection
cur.close()
conn.close()

# --

#           DATA  TYPES        #
# ------------------------------
# SQLITE3 TYPES  |  PYTHON TYPES
# ------------------------------
#    INTEGER     |      INT
#      REAL      |     FLOAT
#      TEXT      |     STRING
#      BLOB      |     BYTES
#      NULL      |      NONE