---
comments: true
date: 2008-04-27 12:49:32
layout: post
slug: installing-ndiswrapper-on-ubuntu-804
title: Installing Ndiswrapper on Ubuntu 8.04
wordpress_id: 369
---

I installed Ubuntu 8.04 today and faced this problem of WiFi again but ths time even installing ndiswrapper diddnt worked so had to find a way to make WiFi work on boot and here it is

For this
1. You need to install ndiswrapper, no need for net coz the packages are included in the CD / DVD of Ubuntu just go to System\>\>Administration\>\>software sources then uncheck all downloadable from internet, Third party and Update repo's make sure you only select Installable from CD-ROM/DVD. 
2. Now open a Add/Remove from Applications\>\>Add/Remove.. there select all avaliable appliactions in show, now seach for ndis you will see Windows Wireless Drivers select it and click Apply changes it will ask you for the CD insert the CD and it will get installed, 
3. now you just have to install the drivers of your card for this open  System\>\>Administration\>\>Windows Wireless Drivers and install the windows wireless drivers ( bcmwl5.inf for hp6515b bcm4312) 

now follow these steps, type

    sudo -i

now you must be as root then type

    gedit /etc/rc.local

the file should read 

    rmmod ndiswrapper
    rmmod ssb
    modprobe ndiswrapper
    exit 0

all done now just reboot and enjoy your Linux...
