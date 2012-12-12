---
comments: true
date: 2009-02-19 00:53:30
layout: post
slug: using-apple-keyboard-in-linux-fedora
title: Using Apple Keyboard in Linux (Fedora)
wordpress_id: 467
---

[![My Apple Keyboard](http://ankurs.com/wp-content/uploads/2009/02/190220091-300x225.jpg)](http://ankurs.com/wp-content/uploads/2009/02/190220091.jpg)

Few Days Ago i received my [Apple Keyboard](http://www.apple.co.in/store/miscAccessories/apple_keyboard.html#overview) and i am enjoying typing on it, but having to hold down the Fn key then tap one of the F-keys to get F-keys working was irritating.

a simple solution to get it working just add this to your /etc/rc.local file

    echo 2 > /sys/module/hid_apple/parameters/fnmode

and F-keys will start to work properly, enjoy

Update :- update for recent kernels,
