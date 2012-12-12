---
comments: true
date: 2006-05-16 00:57:06
layout: post
slug: playing-mp3-on-ubuntu
title: Playing mp3 on UBUNTU
wordpress_id: 91
---

It's usual to find many distributions without MP3 support due to licensing issues. If you have MP3 files and don't know how to play them do the following:
	
* Open the terminal
* Type sudo gedit /etc/apt/sources.list
* Remove comments to packages (This is erasing the # characters in lines starting with ##deb)
* Save changes and close gedit
* Update the packages sudo apt-get update

Install the mulitmedia codecs: 

    sudo apt-get install gstreamer0.8-plugins
    sudo apt-get install gstreamer0.8-lame
    sudo apt-get install gstreamer0.8-ffmpeg
    sudo apt-get install w32codecs
    sudo apt-get install libdivx4linux
    sudo apt-get install lame
    sudo apt-get install sox
    sudo apt-get install ffmpeg
    sudo apt-get install mjpegtools
    sudo apt-get install vorbis-tools gst-register-0.8


Now you can open a player like Rythmbox or Kaffeine and start listening songs.

