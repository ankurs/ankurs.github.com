import urllib, urllib2, time, cPickle

class ialv1:
	interval = 0
	username = ""
	password = ""
	def __init__(self):
		try:
			f = file('ial.info')
			list = cPickle.load(f)
			self.username, self.password = list
			f.close()
		except:
			print "Welcome to I-ON Auto login Script\nMade by Ankur Shrivastava\n"
			self.username = raw_input("Enter Your Username: ")
			self.password = raw_input("Enter Your Password: ")
			list = [self.username,self.password]
			f = file('ial.info','w')
			cPickle.dump(list,f)
			f.close()

	def check(self):
		data = {"loginID":self.username,"loginpassword":self.password,"flag":"0","popcheck":"0","submit":"Sign In"}
                value = urllib.urlencode(data)
                request = urllib2.Request("http://192.168.150.2:8080/clntAuth/clntAuth_main.jsp",value)
		try:
			open = urllib2.urlopen(request)
			print "Logged In"
		except:
			print "Connection Active"

if __name__ == "__main__":
	i = ialv1()
	while (1):
		i.check()
		time.sleep(60)

