---
comments: false
date: 2008-04-12 03:57:33
layout: post
slug: shell-history-stats
title: Shell History Memo
wordpress_id: 361
---

    [ankur@x121 ankur]# history|awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -rn|head
    360 sh
    144 yum
    67 poweroff
    62 nautilus
    41 nano
    26 mysql
    23 python
    18 ssh
    18 exit
    12 kill


PS :- I have a lot of shell scripts made for my daily tasks!!!!!!!
