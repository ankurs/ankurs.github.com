---
comments: true
date: 2010-09-25 23:00:36
layout: post
slug: game-on-weekend-project-iii
title: Game On / Weekend Project III
wordpress_id: 682
tags:
- android
- application
- development
- game
- gaming
- manipal
- mobi
- mobile
- techtatva
- vision
- x11
---

Few weeks ago I posted about playing [pong using tilt sensors on the phone](http://blog.ankurs.com/2010/08/weekend-project-ii/), Now me and [Abhimanyu](http://blog.abhimanyukumar.in/) have taken that to the next level and have made it a generic game controller for any game running on the computer. We faced some problems when Abhimanyu's Samsung Wave refused to work, but luckily i bought a Samsung Galaxy 3 (Android 2.1) about a week before that, so we shifted out focus on Android.

For Game On we make use of the phone's sensors and touch screen to generate different gestures and motion events, we use these events to generate control data and sent the control data over a socket to the computer over a wireless network. On the PC the received data (different for each motion event or gesture) is processed by the computer and a specific task is performed, in this case generating a Key Event.

The Code for Game On can be found on [github](http://github.com/ankurs/Game-On)

Here is a video of the android phone (Samsung I5800 Galaxy 3) being used to control a car racing game.

<iframe width="560" height="315" src="http://www.youtube.com/embed/hWV37mYr6AQ" frameborder="0"> </iframe>

And now the working

<iframe width="560" height="315" src="http://www.youtube.com/embed/D-YqEneKQk8" frameborder="0"> </iframe>

After this we decided to work on something which i wanted to finish a long time ago (remember [Weekend Project I](http://blog.ankurs.com/2010/03/weekend-project/)) so we finished Weekend Project III which is well [Weekend Project I](http://blog.ankurs.com/2010/03/weekend-project/) + [Weekend Project II](http://blog.ankurs.com/2010/08/weekend-project-ii/)

<iframe width="560" height="315" src="http://www.youtube.com/embed/FdNOlLLFLkQ" frameborder="0"> </iframe>

And the working of Weekend Project III

[![Weekend Project III Data Flow](http://files.ankurs.com/Photo0017-300x225.jpg)](http://files.ankurs.com/Photo0017.jpg)

The Data Flow is Phone ----WiFi----> PC ----USB----> USB to [RS232](http://en.wikipedia.org/wiki/RS232) Converter ----[UART](http://en.wikipedia.org/wiki/UART)----> MicroControler ----[Relays](http://en.wikipedia.org/wiki/Relay)----> Toy Car Remote ----RF----> Toy Car, which is almost same as that of [Weekend Project I](http://blog.ankurs.com/2010/03/weekend-project/), except for processing of Sensor Data on Phone.

<iframe width="560" height="315" src="http://www.youtube.com/embed/m2UX83y48YY" frameborder="0"> </iframe>

PS - if you were not able to look at the video's above they can be found [here](http://www.youtube.com/watch?v=hWV37mYr6AQ), [here](http://www.youtube.com/watch?v=D-YqEneKQk8), [here](http://www.youtube.com/watch?v=FdNOlLLFLkQ) and [here](http://www.youtube.com/watch?v=m2UX83y48YY), also Game On won 2nd prize in Mobi Vision - a mobile application development competition

[![MobiVision in TextTatva (by Ed Board Manipal)](http://files.ankurs.com/2010-09-25-17.58.47-300x225.jpg)](http://files.ankurs.com/2010-09-25-17.58.47.jpg)

