---
comments: true
date: 2008-02-17 12:03:19
layout: post
slug: pamp-apache-mysql-php-on-your-phone
title: PAMP -- Apache, MySql, Php on your Phone
wordpress_id: 335
---

![PAMP on Nokia E61i](http://farm3.static.flickr.com/2111/2270106007_97ee524c47.jpg?v=1203229958)


PAMP, an S60 Powered Apache Web Server with PHP and MySQL is available for the S60 3rd edition phones, imagine running a WEB Server on your phone, i saw a few days ago and as i had a supported phone Nokia E61i i was well happy. The supported phone are Nokia E90, Nokia N95 8GB these have 128MB RAM and Nokaia N95 and Nokia E61i with 64MB RAM, well i guess PAMP should run on any S60 3rd Edition device as long as it has 64 MB of ram. The Installation is Simple just [download](http://sourceforge.net/projects/pamp) the `pamp_with_htdocs_on_c.zip` or `pamp_with_htdocs_on_e.zip` depending on where you want your servers root to be. Unzip the file and you will have
	
* `pips_s60_1_2_SS.sis`
* `openc_ssl.sis`
* `PythonForS60_1_4_1_3rdEd.sis`
* `PythonScriptShell_1_4_1_3rdEd.sis`
* `pamp_with_htdocs_on_.sisx`

transfer them to your cell and install them, after the install you will find pamp and connector in your phone menu, click pamp. then start pamp  from `[Options]->[Start]->[Pamp]`, when you see Apache and Mysql running, open your phone browser and goto 127.0.0.1, you will be greeted with a page that says IT WORKS..... congratulations now you have a web server running on your phone for more configuration options you can check the nokia wiki [http://wiki.opensource.nokia.com/projects/PAMP](http://wiki.opensource.nokia.com/projects/PAMP) enjoy!!!!!!!!!

