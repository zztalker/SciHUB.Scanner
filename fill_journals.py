import sqlite3
from scanner import *

con = sqlite3.connect("parser_db");
con.isolation_level = None
cur = con.cursor()


sql = "INSERT INTO journals VALUES ('{sname}','{fname}');"

parser = SIAM_JL_Parser()
parser.feed(str(r.read()))

for j in jl:
	print(sql.format(sname = j.split('/')[2],fname = jl[j]['name']))
	cur.execute(sql.format(sname = j.split('/')[2],fname = jl[j]['name']));

cur.close()


	