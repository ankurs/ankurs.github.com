---
comments: true
date: 2008-02-27 23:53:31
layout: post
slug: configuring-wifi-with-ndiswrapper-on-debian
title: Configuring WiFi with Ndiswrapper on Debian
wordpress_id: 337
---

Note :- If you want the way to make ndiswrapper work just skip the first paragraph its total crap

Well as i have a Broadcom BCM4312 on my HP 6515b laptop, i face a lot of problems with WiFi and the only solution that i know of is using ndiswrapper with makes the windows driver work on Linux, anyway i installed Debian on my laptop around 1 month ago and then never looked back at it, ya i love Fedora, so yesterday when i rebooted my laptop after around a week i saw the Debian entry on my grub i booted into it and tried to connect to the WiFi network which reminded me that i have not configured ndiswrapper and as i have all 3 DVD's of Debian with me i was sure it wont be a problem, but it didnt work and i was left wondering what now, and i started searching the DVD for any other package then i thought ok lets try to build the driver and there i was with a working net in just 5 min

Ok so lets start, you need module-assistant as you have to build the ndiswrapper from the source saperately, so type

    apt-get install module-assistant

then prepare the build environment

    module-assistant prepare

this will download the kernel-header and setup the symbolic links, now install the ndiswrapper-source package

    apt-get install ndiswrapper-source

if you have internet access only via WiFi the download the packages from [http://packages.debian.org](http://packages.debian.org) and then install them, next build ndiswrapper

    module-assistant build ndiswrapper

now type

    apt-get install ndiswrapper-utils-1.9

now you are ready to install the drivers for that follow [this](http://ankurs.com/2007/10/08/using-wifi-in-ubuntu-on-hp-6515b-broadcom/) enjoy
