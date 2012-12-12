---
comments: true
date: 2010-03-11 01:22:34
layout: post
slug: weekend-project
title: Weekend Project
wordpress_id: 607
---

In Dec 2009 at foss.in at the maemo stall i saw a guy control a small toy car through accelerometer on his N900, i thought of replicating that but it just remained in my mind, so last Saturday i finally decided to implement it and went straight to a toy store and bought a toy RF car, one hour of hacking and i was able to control the small car through by phone (Nokia E61i) here is the video of it working.

<iframe width="420" height="315" src="http://www.youtube.com/embed/tdfnt-a7vkM" frameborder="0" > </iframe>

<iframe width="420" height="315" src="http://www.youtube.com/embed/XK8eOvkX14U" frameborder="0" > </iframe>

the concept is simple, i send commands through my phone over wifi to my laptop which controls the car remote, controlling a toy car remote is very easy with a Parallel port and few transistors but laptops don't have parallel ports, so i used a micro-controller in between to sort that out, so now micro controller controls the car remote by acting on signals received over UART from laptop.
the working is Phone ---(WiFi)--->Laptop ---(USB/UART)---> Micro controller ---(Relays)---> Car Remote ---(RF)---> Toy Car
will post details with code sometime later
