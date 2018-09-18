import urllib2

while (True):
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie', 't=XXXXXXXXX'))
	url = 'XXXXXXXXXXXXXXXXX'
	f = opener.open(url)
	stuff = f.read()
	print stuff
