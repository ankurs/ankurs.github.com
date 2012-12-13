import urllib, urllib2, time

username = "Your username"
password = "Your Password"
interval = 10

data = {"loginID":username,"loginpassword":password,"flag":"0","popcheck":"0","submit":"Sign In"}
value = urllib.urlencode(data)
request = urllib2.Request("http://192.168.150.2:8080/clntAuth/clntAuth_main.jsp",value)
print "Logging In\nMade by Ankur - http://ankurs.com"
while (1):
	open = urllib2.urlopen(request)
	responce = open.read()
	for i in range (1,interval):
		print (interval-i),"min Till Next Login"
		time.sleep(60)
	print "Logging In\nMade by Ankur - http://ankurs.com"

