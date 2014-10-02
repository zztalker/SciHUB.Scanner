from connect_db import *
from scanner import *
from md5calc import *

sql = "SELECT Link FROM issues WHERE GetArticles is null;"
sql_i = "INSERT INTO articles (Link,Title,Authors,Citation,DOI, MD5) VALUES ('{Link}','{Title}','{Authors}','{Citation}','{Doi}','{md5}');"

cur.execute(sql.format(link="http://epubs.siam.org/toc/siread/56/1"))
r = cur.fetchall()
j = 0;
for i in r:
	browse_link = i[0]
	j += 1
	print(browse_link)
	r = opener.open(browse_link)
	p = SIAM_I_Parser()
	p.articles = {}
	p.feed(str(r.read()))
	for a in p.articles:
		ad = p.articles[a]	
		md5 = md5code(a.strip("/"))
		print(a,ad)
		cur.execute(sql_i.format(Link=a,Title=ad['title'].replace("'","''"),Authors=ad['authors'].replace("'","''"),Citation=ad['citation'].replace("'","''"),Doi=ad['doi'],md5=md5.md5hex))
	cur.execute("UPDATE issues SET GetArticles=1 WHERE Link = '{link}'".format(link=browse_link))
#	f = open("article "+str(j)+".html","wb")
#	f.write(r.read())
#	f.close()
