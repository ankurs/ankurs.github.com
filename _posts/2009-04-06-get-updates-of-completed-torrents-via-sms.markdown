---
comments: true
date: 2009-04-06 17:43:16
layout: post
slug: get-updates-of-completed-torrents-via-sms
title: Get updates of completed torrents via SMS
wordpress_id: 489
tags:
- dbus
- ktorrent
- Python
- sms
- torrent
- twit
- twitter
---

This Sunday when i was giving [DBUS](http://www.freedesktop.org/wiki/Software/dbus) a look and thinking about all the cool things possible with it, one of my friend came asking how can he control his torrents from anywhere and i thought controlling is ok, do you want SMS updates??, i fired up qdbusviewer and there it was a simple way to get sms notifications of finished torrents using well twitter and ktorrent, so here are the steps

* setup your cell phone to recieve SMS updates in twitter,
* get one more twitter account lets say ktorrent, follow ktorrent and turn device updates on,
* now save the script below say as torrenttwit.py
* now enter this ktorrent account username and password in the script below,
* start ktorrent if not already started, now run the script by typing "python torrenttwit.py"

code  ->

    import dbus,base64,urllib2,urllib
    from dbus.mainloop.glib import DBusGMainLoop
    
    DBusGMainLoop(set_as_default=True)
    username="username"
    password="password"
    
    def tweet(msg):
            request = urllib2.Request('http://twitter.com/statuses/update.json')
            request.add_header('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (username,password))[:-1])
            request.add_data(urllib.urlencode({'status': msg.encode('utf-8')}))
            opener = urllib2.build_opener()
            req= opener.open(request)
    
    s = dbus.SessionBus()
    kt = s.get_object("org.ktorrent.ktorrent","/core")
    
    def update(k):
            torrent = s.get_object("org.ktorrent.ktorrent","/torrent/"+k)
            name = torrent.get_dbus_method("name","org.ktorrent.torrent")
            tweet("ktorrent: finished " +name())
    
    kt.connect_to_signal("finished",update)
    
    import gobject
    loop = gobject.MainLoop()
    loop.run()
    


you are done, now whenever a torrent finishes the script will twit and you will receive an SMS update
enjoy
