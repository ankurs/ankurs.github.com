---
comments: true
date: 2011-09-25 02:42:15
layout: post
slug: weekend-project-iv
title: Weekend Project IV
wordpress_id: 830
---

[![Arduino UNO](http://farm7.static.flickr.com/6163/6179145988_51e62f102e.jpg)](http://www.flickr.com/photos/ankurkingofnet/6179145988/)

Few days back i bought an [Arduino UNO](http://arduino.cc/en/Main/ArduinoBoardUno) board, this is my first Arduino Project and it was damn easy!! I can see the power that Arduino has to offer for hobbyist, i have worked on 8051 and few avr (without Arduino) before, doing stuff with an arduino is pretty easy and straightforward.

In this weekend project i am using a JHD162a (16x2 LCD) connected with Arduino UNO to display the name of the current song being played, i am running mpd on my machine so have used python-mpd to retrieve song info and pyserial to transfer the data over UART to UNO, the UNO just spits out the data received over UART to the LCD.

This is a copy of my earlier project which i did in my third year in college, but that was using a 8051 and i wrote a library (code available [here](https://github.com/ankurs/uC-Dump/blob/master/lcd.asm)) to control the LCD, currently i am using the LiquidCrystal Arduino library for that.

[here](http://www.youtube.com/watch?v=n5dBDtErR34) is the demonstration

<iframe width="420" height="315" src="http://www.youtube.com/embed/n5dBDtErR34" frameborder="0"> </iframe>

UPDATE -> song name, artist and time also added, video [here](http://youtu.be/7rC9crdnKwA) 

<iframe width="420" height="315" src="http://www.youtube.com/embed/7rC9crdnKwA" frameborder="0"> </iframe>

PS - you might also want to see the extremely cheap [CNC machine](http://muditsdiy.blogspot.com/2011/09/sneak-peek-cnc-part-iii.html) being made by one of my friend  
