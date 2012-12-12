---
comments: true
date: 2009-02-13 23:22:23
layout: post
slug: howto-mpd-with-pulse-audio
title: HowTo MPD with Pulse audio
wordpress_id: 453
---

A Little background, i just shifted to [mpd](http://en.wikipedia.org/wiki/Music_Player_Daemon) from Amarok 2.0 somewhy i dont seem to like Amarok 2 but thats a different story, For those who dont know MPD is a flexible, powerful, server-side application for playing music. which runs as a daemon and has a lot of front ends for it, [Sonata](http://sonata.berlios.de/documentation.html) being a popular one.

now coming to the point i use Fedora 10 and it has Pulseaudio by default, now the problem is i some time get  "NO Read Permission" in Sonata and then mpd  would stop working, in mpd.log file i will find "Error opening ALSA device "hw:0,0": Device or resource busy" error, which means this is an pulseaudio permission issue, to solve it we need to change the mpd.conf (/etc/mpd.conf) to

    audio_output {
            type                    "pulse"
            name                    "My Device"
            device                  "hw:0,0"        # optional
            format                  "44100:16:2"    # optional
    }

then we need to add

    load-module module-native-protocol-tcp auth-anonymous=1 

to /etc/pulse/default.pa which gives everybody permission to use pulseaudio and thats it.

NOTE - its like using a Tank to kill a fly but since this is my personal laptop i think this should do just fine
