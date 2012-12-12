---
comments: true
date: 2009-02-16 01:29:10
layout: post
slug: ion-proxy-login-problem
title: ION proxy login problem
wordpress_id: 457
---

a few days ago ION (WiFi provider in Manipal University) started an ISA based proxy using [NTLM](http://en.wikipedia.org/wiki/NTLM) authentication, which was explained to me as a client install!!! some people are facing a lot of problems with it, their browsers are asking for authentication (login) again and again, and repositories are not working on Linux. 

So here is a simple screencast with solution for this problem it works great in Linux (esp. Fedora) i have also included configuring yum here, if someone wants to use apt-get (debian/ubuntu) they can do

     export http_proxy=http://127.0.0.1:5865

Ok coming to the main point, go and download [http://sourceforge.net/projects/ntlmaps/](http://sourceforge.net/projects/ntlmaps/) and then watch the video [here](http://ankurs.com/wp-content/uploads/2009/02/mov1.ogv)

People on windows can install python from [here](http://python.org/ftp/python/2.6.1/python-2.6.1.msi) and then follow the steps
[ION proxy problem solved](http://ankurs.com/wp-content/uploads/2009/02/mov1.ogv)

Note:- If You face any problem please post back here....

PS:- every thing in Text form coming soon... (i am lazy)
