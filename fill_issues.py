from scanner import *
from connect_db import *

sql = "SELECT * from journals;"

sql_ins = "INSERT INTO Issues VALUES ( '{journal}','{num}',{year},'{full_name}','{link}' );"
sql_check = "SELECT Journal, Name, Link FROM issues WHERE Link = '{link}'"

cur.execute(sql)
r = cur.fetchall()
for j in r:
	short_name = j[0]
	browse_link = '/loi/'+short_name
	print(j,browse_link)
	r = opener.open(host+browse_link)
	parser = SIAM_J_Parser()
	parser.issues = {}
	parser.marker = host+'/toc/'+short_name
	parser.feed(str(r.read()))	
	for i in parser.issues:
		full_name = parser.issues[i]['name']
		if ('in Progress' in full_name):
			print("Skip in progress issues")
			continue
		num = full_name.split(',')
		year = num[1]
		num = num[0].strip().split(' ')[1]
		print(i,full_name,"@",num,year)
		cur.execute(sql_check.format(link = i))
		r = cur.fetchone()
		if r == None:
			cur.execute(sql_ins.format(journal = short_name, num = num, year = year, full_name = full_name, link = i))
#		r = opener.open(i)
#		f = open('123.htm','wb')
#		f.write(r.read())
#		f.close()
#		break
cur.close()