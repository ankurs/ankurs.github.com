---
comments: true
date: 2007-05-27 14:00:15
layout: post
slug: using-gprs-with-ubuntu-without-bluetooth-linux-usb-nokia-modem-internet
title: Using GPRS with Ubuntu without Bluetooth on Airtel
wordpress_id: 276
---

Well i know you wont be interested in using GPRS for connecting to net as it offers a download speed of 5KB/s instead of your broadband connection, but it can be of great help when you are traveling or when you dont have a broadband like me ( special thanks to BSNL  for that).

I wanted to install Amarok on my newly installed Ubuntu 7.04 so i needed a net connection for that there were a hell lot of dependency as Amarok is basicly a KDE application. so my hunt began for a way to connect my Nokia 3250 with Airtel MobileOffice to it. I found a hell lot of sites upon searching for it but all of them required me to download some or other package for which i needed a net connection lol, but then on [Linuxquestions.org](http://www.linuxquestions.org/questions/showthread.php?t=555458) i finally found a way to configure it without any extra package just the default Ubuntu Install and guess what it works with all Linux systems (it was originally posted for Fedora). So here is what to do

First:- check the VID and PID of your phone, To do this simpily connect your phone in PcSuit mode through the USB cable provided then type in terminal

    lsusb

to get the output somewhat like this

    ankur@ankur-desktop:~$ lsusb
    Bus 003 Device 001: ID 0000:0000
    Bus 002 Device 002: ID 0421:042d Nokia Mobile Phones
    Bus 002 Device 001: ID 0000:0000
    Bus 001 Device 001: ID 0000:0000

Notice the ID 0421:042d Nokia Mobile Phones here 421 is the VID and 42d is the PID replace them with what is shown in your case below. Now run the command

    sudo /sbin/modprobe usbserial vendor=0x(vid) product=0x(pid)

Like "sudo /sbin/modprobe usbserial vendor=0x421 product=0x42d" in my case

then run the following command

    wvdialconf create

To get the following output

    ankur@ankur-desktop:~$ sudo wvdialconf create
    Scanning your serial ports for a modem.
    Port Scan: S0 S1 S2 S3
    WvModem: Cannot get information for serial port.
    ttyACM0: ATQ0 V1 E1 -- OK
    ttyACM0: ATQ0 V1 E1 Z -- OK
    ttyACM0: ATQ0 V1 E1 S0=0 -- OK
    ttyACM0: ATQ0 V1 E1 S0=0 &C1 -- OK
    ttyACM0: ATQ0 V1 E1 S0=0 &C1 &D2 -- OK
    ttyACM0: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 -- OK
    ttyACM0: Modem Identifier: ATI -- Nokia
    ttyACM0: Speed 4800: AT -- OK
    ttyACM0: Speed 9600: AT -- OK
    ttyACM0: Speed 19200: AT -- OK
    ttyACM0: Speed 38400: AT -- OK
    ttyACM0: Speed 57600: AT -- OK
    ttyACM0: Speed 115200: AT -- OK
    ttyACM0: Speed 230400: AT -- OK
    ttyACM0: Speed 460800: AT -- OK
    ttyACM0: Max speed is 460800; that should be safe.
    ttyACM0: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 -- OK
    Found an USB modem on /dev/ttyACM0.
    Modem configuration written to create.
    ttyACM0: Speed 460800; init "ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0"

This shows that a modem is connected at /dev/ttyACM0, Now substitute this at (your modem) in the script below

Enter the command

    sudo gedit etc/wvdial.conf

delete any thing already written there and place this in that

    [Dialer Defaults]
    Modem = (your modem)
    Baud = 230400
    Init1 = ATZ
    Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    ISDN = 0
    Modem Type = Analog Modem
    Phone = *99***1#
    Username = A
    Password = B
    Stupid Mode = 1

All done now to connect  open terminal and type `sudo wvdial` and you are connected with the following output

    ankur@ankur-desktop:~$ sudo wvdial
    Password:
    --> WvDial: Internet dialer version 1.56
    --> Cannot get information for serial port.
    --> Initializing modem.
    --> Sending: ATZ
    ATZ
    OK
    --> Sending: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    OK
    --> Modem initialized.
    --> Sending: ATDT*99***1#
    --> Waiting for carrier.
    ATDT*99***1#
    CONNECT
    ~[7f]}#@!}!} } }2}#}$@#}!}$}%\}"}&} }*} } g}%~
    --> Carrier detected.  Starting PPP immediately.
    --> Starting pppd at Sat May 26 23:56:24 2007
    --> Pid of pppd: 5682
    --> Using interface ppp0
    --> pppd: �[06][06][08][06][08]
    --> pppd: �[06][06][08][06][08]
    --> pppd: �[06][06][08][06][08]
    --> pppd: �[06][06][08][06][08]
    --> pppd: �[06][06][08][06][08]
    --> local  IP address 10.190.137.17
    --> pppd: �[06][06][08][06][08]
    --> remote IP address 10.6.6.6
    --> pppd: �[06][06][08][06][08]
    --> primary   DNS address 202.56.230.5
    --> pppd: �[06][06][08][06][08]
    --> secondary DNS address 202.56.240.5
    --> pppd: �[06][06][08][06][08]


To disconnect press Ctrl+C
