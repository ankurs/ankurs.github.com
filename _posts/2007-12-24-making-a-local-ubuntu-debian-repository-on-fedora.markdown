---
comments: true
date: 2007-12-24 22:26:38
layout: post
slug: making-a-local-ubuntu-debian-repository-on-fedora
title: Making a local Ubuntu / Debian repository on Fedora
wordpress_id: 323
---

So now i know how to make a local Ubuntu / Debian LAN repository on Fedora using apt-cacher, apt-cacher as the name says caches all the packages with it when ever any client requests a package from it, it checks if the package that is there with it is latest or not if it is then it serves that package else it downloads the package and serves it, but well i am not discussing what it does here but how to set it up on Fedora 8, so lets begin

for apt-cacher to work you need to have a apache server installed and the source of apt-cacher which can be downloaded from [here](http://packages.debian.org/etch/apt-cacher) just and extract it and follow the following step as root

    mv apt-cacher-1.5.3 /usr/share/apt-cacher

here 1.5.3 was the latest package during my writing, then rename apache.conf to /etc/httpd/conf.d/apt-cacher.conf and set the permisions

    cd /usr/share/apt-cacher
    mv apache.conf /etc/httpd/conf.d/apt-cacher.conf
    chmod 644 /etc/httpd/conf.d/apt-cacher.conf
    chown root:root /etc/httpd/conf.d/apt-cacher.conf

now just restart apache

    /etc/init.d/httpd restart

now rename apt-cacher2 to apt-cacher and move all the .conf files to /etc/apt-cacher/

    mv apt-cacher2 apt-cacher
    mkdir /etc/apt-cacher
    mv *.conf /etc/apt-cacher/

now edit /etc/httpd/conf.d/apt-cacher.conf and edit user and group to apache

    gedit /etc/httpd/conf.d/apt-cacher.conf

after doing that run install.pl

    ./install.pl

now make /var/cache/apt-cacher and /var/log/apt-cacher owned by apache

    chown -R apache /var/cache/apt-cacher
    chown -R apache /var/log/apt-cacher

all done just goto http://yourip/apt-cacher and every thing should work fine, if it does not then check /var/log/http/error_log for what went wrong and dont forget to forward the port 3142 (default) so that everyone can access it

you can see how to configure it [here](http://www.debuntu.org/how-to-set-up-a-repository-cache-with-apt-cacher) and since you are on Fedora you will have to modify some steps a little

enjoy

