---
comments: true
date: 2008-09-16 22:58:42
layout: post
slug: ion-auto-login-script-python
title: Ion Auto Login script in Python
wordpress_id: 399
---

i was just thinking about making the very famous IAL script of DJ in python and here is it and its damn simple
    
    <code>import urllib, urllib2, time
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
    </code>



or [downlaod](http://files.ankurs.com/ial.py)

run it by typing `python ial.py`

it uses urllib, urllib2 and time which are the default module, you have to change the username and password to your username and password, changing the interval changes the time interval in which auto login takes place. 

PS - current it does no check if your connection is active or not, will add that soon
