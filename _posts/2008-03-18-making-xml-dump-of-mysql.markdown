---
comments: true
date: 2008-03-18 15:50:06
layout: post
slug: making-xml-dump-of-mysql
title: Making Xml dump of MySQL
wordpress_id: 346
---

Yesterday when i was trying/searching for a way to generate XML file from PHP so as to use it in Project 11, i came across a way to make a direct database/table dump from mysql and its damn easy all you have to do is type

    mysqldump -u username -p --xml databasename > data.xml

and it will dump whole database into the data.xml file 

PS:- Info about Project 11 coming up.....
