import sqlite3

con = sqlite3.connect("parser_db");
con.isolation_level = None
cur = con.cursor()
