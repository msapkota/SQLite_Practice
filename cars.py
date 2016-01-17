import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor().execute("CREATE TABLE INVENTORY (Make TEXT, Model TEXT, Quantity INT)")

#cursor.execute("CREATE TABLE INVENTORY (Make TEXT, Model TEXT, Quantity INT)")

conn.close()
