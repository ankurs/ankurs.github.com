---
comments: true
date: 2008-02-25 19:24:49
layout: post
slug: enabling-wifi-on-lenovo-r60-in-linux
title: Enabling Wifi on Lenovo R60 in Linux
wordpress_id: 336
---

So yesterday after hunting for the solution of the wifi problem in Lenovo R60 so quite sometime i finally decided to try [DJays](http://djkaos.wordpress.com/) solution to build [Madwifi](http://madwifi.org/) and it worked like a charm. I was thinking that there will be a total Open Source solution of the problem but well i just hope that ath5k will replace madwifi soon, anyway here is something about MadWifi


> MadWifi is one of the most advanced WLAN drivers available for Linux today. It is stable and has an established userbase. The driver itself is open source but depends on the proprietary Hardware Abstraction Layer (HAL) that is available in binary form only.


Ok so lets start, first you need to download the source of Madwifi, go to [http://madwifi.org/wiki/UserDocs/GettingMadwifi](http://madwifi.org/wiki/UserDocs/GettingMadwifi) and download tar.gz source package, extract it now open a terminal and login as root by typing su or sudo -i, then goto the madwifi directory and type

    cd scripts
    ./find-madwifi-modules.sh $(uname -r)
    cd ..

now you are ready to compile

    make

now to install type

    make install

Now load the module

    /sbin/modprobe ath_pci

now you can easily connect to the net on your Lenovo R60 lappy

If you want to enable the wifi led just edit /etc/sysctl.conf, type

    gedit /etc/sysctl.conf

and add this at the end of the file and save

    dev.wifi0.ledpin=1
    dev.wifi0.softled=1

reboot and thats it enjoy!
