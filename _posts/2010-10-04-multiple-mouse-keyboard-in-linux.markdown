---
comments: true
date: 2010-10-04 02:03:26
layout: post
slug: multiple-mouse-keyboard-in-linux
title: multiple mouse / keyboard in linux
wordpress_id: 709
---

[![4 mouse cursors on a single screen](http://files.ankurs.com/mpx-300x225.jpg)](http://files.ankurs.com/mpx.jpg)

few days ago i came upon an article about human computer interactions which mentioned different ways we interact with computes and how we will interact with computers in future, the article instantly reminded me of [MPX](http://en.wikipedia.org/wiki/Multi-Pointer_X), now i dont know how many of you remember [MPX](http://en.wikipedia.org/wiki/Multi-Pointer_X) which enabled interaction of multiple mouse/keyboards in linux. [Xserver](http://en.wikipedia.org/wiki/X_Window_System) 1.7 which is used in most of the disto's was released with MPX, so i decided to find out how to make it work on my existing Fedora 13 box, and using it is pretty simple you just need to use xinput and configure X for multiple input, for that you first need to install xinput, on fedora it is provided by the package "xorg-x11-apps" just do a 
    
    [ankur@x144 ankur]# yum install xorg-x11-apps -y

and you are done, for other distro's i guess there sould be a similar package, after the install we need to find what all is plugged in to the computer, for that we do "xinput list"

    
    [ankur@x144 ankur]# xinput list
    ⎡ Virtual core pointer                        id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                  id=4    [slave  pointer  (2)]
    ⎜   ↳ PS/2 Mouse                                  id=14    [slave  pointer  (2)]
    ⎜   ↳ AlpsPS/2 ALPS GlidePoint                    id=15    [slave  pointer  (2)]
    ⎣ Virtual core keyboard                       id=3    [master keyboard (2)]
    ↳ Virtual core XTEST keyboard                 id=5    [slave  keyboard (3)]
    ↳ Video Bus                                   id=6    [slave  keyboard (3)]
    ↳ Power Button                                id=7    [slave  keyboard (3)]
    ↳ Sleep Button                                id=8    [slave  keyboard (3)]
    ↳ Laptop Integrated Webcam                    id=9    [slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard                id=13    [slave  keyboard (3)]
    ↳ Dell WMI hotkeys                            id=16    [slave  keyboard (3)]


this returns a list of all the input devices, i am running this on my laptop so you can see "AlpsPS/2 ALPS GlidePoint" and "AT Translated Set 2 keyboard" which are my laptop's mouse and keyboard, to enable multiple keyboard/mouse i will create a group and move my laptops mouse and keyboard to the group, 

    
    [ankur@x144 ankur]# xinput create-master main
    [ankur@x144 ankur]# xinput list
    ⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
    ⎜   ↳ PS/2 Mouse                              	id=14	[slave  pointer  (2)]
    ⎜   ↳ AlpsPS/2 ALPS GlidePoint                	id=15	[slave  pointer  (2)]
    ⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
        ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
        ↳ Video Bus                               	id=6	[slave  keyboard (3)]
        ↳ Power Button                            	id=7	[slave  keyboard (3)]
        ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
        ↳ Laptop Integrated Webcam                	id=9	[slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard            	id=13	[slave  keyboard (3)]
        ↳ Dell WMI hotkeys                        	id=16	[slave  keyboard (3)]
    ⎡ main pointer                          	id=10	[master pointer  (11)]
    ⎜   ↳ laptop XTEST pointer                    	id=12	[slave  pointer  (10)]
    ⎣ main keyboard                         	id=11	[master keyboard (10)]
        ↳ laptop XTEST keyboard                   	id=17	[slave  keyboard (11)]
    


above i created a group by the name "main", you can see a second mouse cursor on screen as soon as you do this, to make both these mouse/keyboard active i will move my laptop's mouse (id-> 15) and keyboard (id-> 13) to this newly created group

    
    [ankur@x144 ankur]# xinput reattach 15 10
    [ankur@x144 ankur]# xinput reattach 13 11


now if i connect an external mouse and keyboard to my laptop i can see both working simultaneously, if you want multiple (more then 2) mouse and keyboards to work, you can create a separate group for them and move them to that group in a similar manner.
after doing this I was not able to find any benefit of using multiple mouse/keyboard on a laptop but it will make sense when you have multi monitor setup and multiple users trying to use the same machine simultaneously.
