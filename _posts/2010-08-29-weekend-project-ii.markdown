---
comments: true
date: 2010-08-29 21:52:33
layout: post
slug: weekend-project-ii
title: Weekend Project II
wordpress_id: 656
tags:
- bada
- game
- phone
- pong
- project
- qt
- samsung
- sensors
- tilt
- weekend
---

In march i posted about a [weekend project](http://ankurs.com/2010/03/weekend-project/) which involved controlling a small toy car using my cell phone, this is a similar one again implemented in few hours, here we are trying to play the awesome game of pong using the tilt sensor on Samsung Wave. The pong application running on Laptop is written in [Qt](http://qt.nokia.com/) (C++) and the application on the Phone is written using the [Bada SDK](http://www.bada.com/).

The working is simple, the pong application running on Laptop requires phones to make a TCP connection to it. Phones just create a TCP connection to the application on PC and sends tilt sensor data to it, movement of paddles is done by the PC application based on the value it receives from the phones. It still **requires better calibration** and we will work on it after the exams are over (Education prevents you from doing cool things!!), there are a lot of ideas buzzing in our empty heads (according to our teachers!!) , the original idea was by [Abhimanyu](http://abhikumar777.blogspot.com/) which we implemented.

<iframe width="560" height="315" src="http://www.youtube.com/embed/dHinEjh8iIw" frameborder="0"> </iframe>

<iframe width="420" height="315" src="http://www.youtube.com/embed/Aw15OuquzcQ" frameborder="0" > </iframe>

if you cannot see the above video [here](http://www.youtube.com/watch?v=dHinEjh8iIw) and [here](http://www.youtube.com/watch?v=Aw15OuquzcQ) are short demo of how it works.

PS - code and proper working for the previous and this weekend project will be posted soon!
