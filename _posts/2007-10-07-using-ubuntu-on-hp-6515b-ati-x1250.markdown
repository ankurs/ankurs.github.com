---
comments: true
date: 2007-10-07 00:40:16
layout: post
slug: using-ubuntu-on-hp-6515b-ati-x1250
title: Using Ubuntu on HP 6515b ( ATI X1250 )
wordpress_id: 295
---

So there are a lot of people having trouble installing Linux ( Ubuntu ) on those ATI Radeon Xpress 1250 or any other ATI card here is the solution ( i have given this example with ubuntu but it can be used with any other Linux distro ) first go to ATI's site and [download the driver](http://ati.amd.com/support/driver.html) then all we have to do is boot into your linux distro and just install the drivers, for that we will first need a copy of the drivers on HDD or flash drive, and then just cd into that directory and type

    sh ati-driver-installer-8.40.4-x86.x86_64.run

where ati-driver-installer-8.40.4-x86.x86\_64.run is the name of the driver file with me, it will start the install procedure just follow that and after the install just configure your resolution with

    aticonfig --resolution=0,1280x800

as my resolution was 1280x800 your can be 1024x786 or some other just type what ever it is.

after this we just need to start the X server again type `startx` and enjoy every thing in graphical mode.

Note:- if you used a Live CD you will have to install the drivers 2 times first for the live CD and then for your system, enjoy!!!


