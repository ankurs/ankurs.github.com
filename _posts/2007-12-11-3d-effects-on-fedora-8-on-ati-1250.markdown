---
comments: true
date: 2007-12-11 01:29:40
layout: post
slug: 3d-effects-on-fedora-8-on-ati-1250
title: 3D effects on fedora 8 on ati 1250
wordpress_id: 320
---

I have finally found a way to make Compiz work on ATI x1250 on HP 6515b after searching on a large number of forums i finally found it on [Fedora Forums](http://forums.fedoraforum.org/showthread.php?t=155503) all thanks to [leigh123@linux](http://forums.fedoraforum.org/forum/member.php?u=78273) and here is my easy way well its not that easy but still  it works 

PLEASE TRY THIS  PROCEDURE CAREFULLY IT HAS NOT WORKED ON SOME SYSTEMS  I WILL UPDATE IT AS AND WHEN I GET A DIFFERENT WAY 

First enable the Livna repositories type

    su -c 'rpm -Uhv http://rpm.livna.org/livna-release-8.rpm'

then type

    yum install kmod-fglrx xorg-x11-drv-fglrx xorg-x11-drv-fglrx-libs-32bit
    yum update kmod-fglrx xorg-x11-drv-fglrx xorg-x11-drv-fglrx-libs-32bit
    service fglrx restart
    fglrx-config-display enable

now restart your xserver by pressing ctrl + alt + backspace , then after restarting go to terminal type

    fglrxinfo

you should see something like this

    display: :0.0  screen: 0
    OpenGL vendor string: ATI Technologies Inc.
    OpenGL renderer string: ATI Radeon X1200 Series
    OpenGL version string: 2.0.6958 Release

and then run

    glxinfo

you should see some thing like this

    name of display: :0.0
    display: :0  screen: 0
    ** direct rendering: Yes**
    server glx vendor string: SGI
    server glx version string: 1.2
    server glx extensions:
    GLX_ARB_multisample, GLX_EXT_import_context, GLX_EXT_texture_from_pixmap,
    GLX_EXT_visual_info, GLX_EXT_visual_rating, GLX_OML_swap_method,
    GLX_SGIS_multisample, GLX_SGIX_fbconfig, GLX_SGIX_visual_select_group
    client glx vendor string: SGI
    client glx version string: 1.4
    .......................................................

now you can proceed with update of Compiz, for this add the compiz fusion repo login as root and type

    wget http://www.dfm.uninsubria.it/compiz/fusion/compiz-fusion.repo
    cp compiz-fusion.repo  /etc/yum.repos.d/

before install remove the old packages type

    rm -rf /home/*/.config/compiz
    rm -rf /home/*/.gconf/apps/compiz

now install compiz

    yum install compiz-all fusion-icon-all compiz-fusion-plugins-unsupported compiz-bcop ccsm emerald-themes

after this we have to downgrade  xorg-x11-server-Xorg for all i386 (32bit) users type

    wget http://koji.fedoraproject.org/packages/xorg-x11-server/1.3.0.0/9.fc7/i386/xorg-x11-server-Xorg-1.3.0.0-9.fc7.i386.rpm
    rpm -U --oldpackage xorg-x11-server-Xorg-1.3.0.0-9.fc7.i386.rpm

For `x86_64` (64bit) users type

    wget http://koji.fedoraproject.org/packages/xorg-x11-server/1.3.0.0/9.fc7/x86_64/xorg-x11-server-Xorg-1.3.0.0-9.fc7.x86_64.rpm
    rpm -U --oldpackage xorg-x11-server-Xorg-1.3.0.0-9.fc7.x86_64.rpm

now we have to prevent xorg-x11-server-Xorg from upgrading so we blacklist it

    gedit /etc/yum.conf

add

    exclude=xorg-x11-server-Xorg

at the end, thats it!

PS:- Dont enable too many plugins it will slow things down and there is some problem that i face with the Expo plugin dont enable that

