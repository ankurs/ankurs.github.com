---
comments: true
date: 2007-10-16 14:10:39
layout: post
slug: problem-with-gtalk-in-kopete
title: Problem with Gtalk in Kopete
wordpress_id: 298
---

some people have trouble connecting to Gtalk on Kopete here is hoe to do it.

* Open Kopete go to Settings\>\>configure\>\>accounts
* Add a new Jabber account.
* Enter your complete Google Mail address and corresponding password.
* go to the Connection page of the dialog.
* check "Use protocol encryption (SSL)" checkbox
* check "Allow plain-text password authentication" checkbox
* check "override default server information" checkbox
* and set server to "talk.google.com port 5223, If you are behind a firewall and can't connect to the 5223 port you can use the 443 port (standard SSL port).

there you are all set to connect and enjoy

NOTE :- if you recive some sort of SSL errors just install the qca-tls package by 'sudo apt-get install qca-tls' in debian/Ubuntu

