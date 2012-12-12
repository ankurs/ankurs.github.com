---
comments: true
date: 2008-09-17 17:45:48
layout: post
slug: ion-auto-login-script-in-python-version-1
title: ION Auto Login Script in Python Version 1
wordpress_id: 406
---

After yesterdays efforts i have now made a complete working Python IAL (ION Auto Login) script which can store your password and checks for login in every 1 Min and continues till you stop it, here is the Code

    iimport urllib, urllib2, time, cPickle
    
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
                    bol =1
                    while (bol ==1):
                            try:
                                    open = urllib2.urlopen(request)
                                    print "Logged In"
                                    bol = 2
                            except:
                                    print "Server Gone Crazy\ntrying again...."
    
    if __name__ == "__main__":
            i = ialv1()
            while (1):
                    i.check()
                    time.sleep(60)
    

You can Download it [here](http://fb.ankurs.com/ialv1.py)

