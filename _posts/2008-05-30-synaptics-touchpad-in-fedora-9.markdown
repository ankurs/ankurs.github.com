---
comments: true
date: 2008-05-30 10:00:35
layout: post
slug: synaptics-touchpad-in-fedora-9
title: Synaptics Touchpad in Fedora 9
wordpress_id: 374
---

I have been using Fedora 9 from a long time and it really kick's ass but i was facing the problem that my Touchpad was not working with it but the i found the solution [here](http://gentoo-wiki.com/HARDWARE_Synaptics_Touchpad)

The easiest was will be to install the package [http://atrpms.net/dist/f9/synaptics/](http://atrpms.net/dist/f9/synaptics/) 

or you can do it manually here

edit the /etc/X11/xorg.conf

    gedit /etc/X11/xorg.conf

Added the following to the ServerLayout Section

    InputDevice “TouchPad” “CorePointer”

add a new section:

    Section “InputDevice”
    Driver      “synaptics”
    Identifier  “TouchPad”
    Option      “SendCoreEvents”
    Option      “Protocol” “auto-dev”
    Option      “SHMConfig” “on”
    Option “TapButton1″ “1″
    Option “TapButton2″ “2″
    EndSection

all done logout and login again and everything should be working fine

Update: found the rpm package [here](https://bugzilla.redhat.com/show_bug.cgi?id=439386#c66)

