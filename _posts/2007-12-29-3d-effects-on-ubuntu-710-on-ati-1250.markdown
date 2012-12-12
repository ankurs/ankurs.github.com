---
comments: true
date: 2007-12-29 01:46:14
layout: post
slug: 3d-effects-on-ubuntu-710-on-ati-1250
title: 3D effects on ubuntu 7.10 on ati 1250
wordpress_id: 324
---

Well after going through a large number of guides like [this](http://www.blog.arun-prabha.com/2007/12/11/yet-another-guide-for-compiz-ati-ubuntu-gutsy/) i finally thought about giving guide at [cchtml](http://wiki.cchtml.com/index.php/Ubuntu_Gutsy_Installation_Guide) a try, well the hings mentioned are really great but not all steps are needed so here is a simplified version

Here i assume that you have not done any of this step before and are doing it for the first time but if that is not the case then this **might** not work for you.
Ok so first step installation of drivers, there are two steps for this as mentioned in the cchtml wiki one automatic and other manual, for automatic you  need to enable the restricted repositories by going to System>>Administration>>Software Sources, and the typing

    sudo apt-get update
    sudo apt-get install linux-restricted-modules-generic restricted-manager
    sudo apt-get install xorg-driver-fglrx

which will install the drivers by downloading them from net, if you dont have the bandwidth to download that much you can go for the manual install where we will build those file, here i assumed that you have copy of the ati drivers **.run** file which if your Ubuntu is installed by me could be found at "/", to build we need to install certain packages

    `sudo apt-get install module-assistant build-essential fakeroot dh-make debhelper debconf libstdc++5 linux-headers-generic dkms`

to build the packages type
    `sudo bash ati-driver-installer-8.443.1-x86.x86_64.run --buildpkg Ubuntu/gutsy`

in the directory where you have the ati-driver-installer-8.443.1-x86.x86_64.run file, this is the latest file at the time of writing but you might have a different file this will work with any driver after 8.38, as they have AIGLX support anyway now we need to install the packages made type

`sudo dpkg -i xorg-driver-fglrx_8.443.1-1*.deb fglrx-kernel-source_8.443.1-1*.deb fglrx-amdcccle_8.443.1-1*.deb`

when you do that you might be asked

    Configuration file '/etc/xdg/compiz/compiz-manager'
    ==> Deleted (by you or by a script) since installation.
    ==> Package distributor has shipped an updated version.
    What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
    D     : show the differences between the versions
    Z     : background this process to examine the situation
    The default action is to keep your current version.
    *** compiz-manager (Y/I/N/O/D/Z) [default=N] ?
    
just answer Y to the question and proceed, once this is done you now need to edit the xorg.conf file type 

    aticonfig --initial
    sudo gedit /etc/X11/xorg.conf

and replace

    Section "Device"
    Identifier  "Generic Video Card"
    Driver      "vesa"
    BusID       "PCI:1:5:0"
    EndSection

WITH

    Section "Device"
    Identifier  "Generic Video Card"
    #Driver      "vesa"
    BusID       "PCI:1:5:0"
    Option		"VideoOverlay"		"on"
    Option		"OpenGLOverlay"		"off"
    EndSection 

now just restart the X server but pressing Ctrl + ALT + Backspace, all done this will give you the Basic 3D effects but who is satisfied with  that we need more so we will go for installing Compiz settings manager, for this type

    sudo apt-get install compizconfig-settings-manager gcompizthemer subversion
    svn ls https://svn.generation.no/emerald-themes

now accept the certificate and fetch the themes by going to System>>Preferances>>Emerald Themes Manager, to enable 3D effects go to System>>Preferances>>Appearance then Visual Effects select Custom and edit your settings by Preferances, now you are all set to blow  everyone up with your Linux box's 3D effects enjoy
