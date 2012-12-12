---
comments: true
date: 2008-09-27 17:52:07
layout: post
slug: using-yum-with-a-proxy-fedora
title: Using YUM with a proxy Fedora
wordpress_id: 414
---

Finally i got a chance to use the awesome LAN at the college campus and it was a very good time to update the packages, but there was a problem it had a proxy, so i typed man yum and was pointed at man yum.conf and there it was a simple solution, all the you need to do is just edit the yum.conf file as root

type

    su

enter your root password now type

    gedit /etc/yum.conf

here add a line

    proxy = http://address:port

replace the above code with the address you need like 172.16.19.10 and port 80 in my case and all will work just fine

