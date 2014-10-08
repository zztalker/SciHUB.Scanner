from connect_db import *
from scanner import *
from md5calc import *
import gzip,os

sql = "SELECT Link,MD5 From articles WHERE  Loaded=0"
sql_u = "UPDATE articles SET Loaded = 1 WHERE Link = '{link}'"

cur.execute(sql)
for a in cur.fetchall():
	md5hex = md5code(a[0].strip('/').lower())
	print(a[0])
	r = opener.open(host+a[0])
	b = r.read()
	if not os.path.exists(md5hex.byte1+"\\"+md5hex.byte2):
		os.makedirs(md5hex.byte1+"\\"+md5hex.byte2)
	f = gzip.open(md5hex.byte1+"\\"+md5hex.byte2+"\\"+md5hex.md5hex+".html.gz","wb")
	f.write(b.strip())
	f.close()
	cur.execute(sql_u.format(link=a[0]))


