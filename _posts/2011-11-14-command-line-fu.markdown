---
comments: true
date: 2011-11-14 00:16:12
layout: post
slug: command-line-fu
title: Command Line Fu
wordpress_id: 847
tags:
- lock
- screen
- timeout
- x11
- xkcd
---
<img src='http://ankurs.com/wp-content/uploads/2011/11/command_line_fu.png' width='90%' />

A few weeks back i bought a new monitor Dell U2312HM, its a brilliant monitor with support for portrait/landscape switching.
so as it always happens after buying a new monitor i planned a movie night and ran into the screen lock problem, i have set 2 minute timeout for screen lock and some why changing screen settings didn't work, i knew i had to find a solution and fast or the above xkcd might actually happen with me

so this is what i came up with, having worked with X bindings before for [Game-on](http://ankurs.com/2010/09/game-on-weekend-project-iii/) this was done in under 5 mins (after reading some docs) , another day saved all thanks to Linux, X11 and previous X11 binding experience :P

This code moves the mouse pointer back and forth every few seconds, which is defined in DURATION
<script src="https://gist.github.com/1362439.js?file=movietime.c"> </script>
