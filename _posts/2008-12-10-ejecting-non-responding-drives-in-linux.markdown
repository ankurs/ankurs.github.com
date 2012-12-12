---
comments: true
date: 2008-12-10 00:11:13
layout: post
slug: ejecting-non-responding-drives-in-linux
title: Ejecting non responding drives in Linux
wordpress_id: 428
---

One of the biggest (not necessarily) problems that most (new) Linux users face is the problems of non responsive drives, espically when u insert a curropt CD / DVD which refuse to come out because something is trying to access it... or the extremely slow flash drives there are some software for it in windows like Unlocker ( dont remmember the correct name scine i dont use it ) but here we dont need any specific software we have had that feature from a long time and well its as simple as 2-3 lines on terminal and its name is " **fuser** " which is basicly used to displays the PIDs of processes using the specified files or file systems. and we can easily use it for our perpose, lets take an example suppose we need to remove the non responsing CD, for that you need to be root, do

    su -

or

    sudo -i

then type 

    fuser -k /dev/sr0

or 

    fuser -k /dev/cdrom0

which will kill all the process accessing that particular device, now you can easily eject the by doing

    eject /dev/sr0

or

    eject /dev/cdrom0

and you are done.

PS - " fuser " is useful in many more ways then just ejecting drives see " man fuser " for more info

