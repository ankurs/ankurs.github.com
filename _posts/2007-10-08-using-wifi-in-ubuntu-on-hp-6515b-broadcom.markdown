---
comments: true
date: 2007-10-08 23:12:08
layout: post
slug: using-wifi-in-ubuntu-on-hp-6515b-broadcom
title: Using Wifi in Ubuntu on HP 6515b (broadcom)
wordpress_id: 296
---

after the install the thing that is left is the WiFi support for that

first disable the bcm43xx driver

    sudo rmmod bcm43xx

then black list the driver by adding "balcklist bcm43xx" in

    sudo gedit /etc/modprobe.d/blacklist

then download diswrapper-utils-1.9 deb file and install it offline or if you have a LAN connection, For the next step you should have a copy of the windows driver on HDD or flash drive and type

    sudo ndiswrapper -i /the location of windows driver/bcmwl5.inf

now check if driver is there or not

    sudo ndiswrapper -l

you should get a output like

    bcmwl5 : driver installed
    device (14E4:4312) present (alternate driver: bcm43xx)

then type

    sudo ndiswrapper -m

to write wlan0 to ndiswrapper, then you need to start ndiswrapper type

    sudo modprobe ndiswrapper

Now you just need to enable ndiswrapper to start on boot, for that add "ndiswrapper" in /etc/modules

    sudo gedit /etc/modules

all done enjoy
