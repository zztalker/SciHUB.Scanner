from connect_db import *
from scanner import *
from md5calc import *
import gzip,os

sql = "SELECT Link,MD5 From articles WHERE  Loaded=0 and Link = '/doi/abs/10.1137/1102023'"

cur.execute(sql)
for a in cur.fetchall():
	md5hex = md5code(a[0].strip('/').lower())
	print(a[0])
	r = opener.open(host+a[0])
	b = r.read()
	if not os.path.exists(md5hex.byte1+"\\"+md5hex.byte2):
		os.makedirs(md5hex.byte1+"\\"+md5hex.byte2)
	f = gzip.open(md5hex.byte1+"\\"+md5hex.byte2+"\\"+md5hex.md5hex+".html.gzip","wb")
	f.write(b)
	f.close()


