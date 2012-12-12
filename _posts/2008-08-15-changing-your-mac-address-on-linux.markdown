---
comments: true
date: 2008-08-15 00:01:16
layout: post
slug: changing-your-mac-address-on-linux
title: Changing your mac address on Linux
wordpress_id: 392
---

I have seen a lot of people saying that "you can never change your mac its in the hardware, you dont have access to it", but well you can easily change you mac on Linux with a simple command **ifconfig**. Which is mainly used to configure  the kernel-resident network interfaces and it can help you change your mac first see your current mac type as root

    ifconfig

here see your mac address in the following out put

    wlan0     Link encap:Ethernet  HWaddr 00:2B:B5:43:A5:12
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)

where wlan0 is the network interface and " 00:2B:B5:43:A5:12 " is your mac address, next you need to bring the network interface down by typing

    ifconfig wlan0 down

here replace wlan0 with the network interface you are using, normally it is wlan0 for WiFi and eth0 for Ethernet, now its time to change your mac address, simply type

    ifconfig wlan0 hw ether 00:2B:B5:43:A5:3D

here replace 00:2B:B5:43:A5:3D with the mac ID you want to use and then bring the network interface up

    ifconfig wlan0 up

now again see the output of " ifconfig " to check that now you HWaddr has changed from 00:2B:B5:43:A5:12 to 00:2B:B5:43:A5:3D

PS - MAC = Media Access Control
