import csv
import sqlite3

with sqlite3.connect("new.db") as conn:
  c = conn.cursor()

  employees = csv.reader(open("employees.csv", "rU"))

  c.execute("CREATE TABLE IF NOT EXISTS EMPLOYEES(firstname TEXT, lastname TEXT)")

  c.executemany("INSERT INTO employees VALUES(?,?)", employees)
