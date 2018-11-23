import urllib2

while (True):
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie', 't=XXXXXXXXX'))
	url = 'XXXXXXXXXXXXXXXXX'
	f = opener.open(url)
	site = f.read()
	print (site)
