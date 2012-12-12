---
comments: true
date: 2007-12-04 13:15:28
layout: post
slug: twit-from-command-line-linux
title: Twit from command line (Linux)
wordpress_id: 313
---

Here is a thing that i found during searching for a completely different things, you can update your Twitter status simply by using curl which is most of the time installed by default so here is the command

    /usr/bin/curl -u username:password -d status="your tweet" http://twitter.com/statuses/update.xml

it simply updates your twitter status, this is extremely simple and could easily be used to update status, but the problem is that it contains your password   and you dont want to display your password so you can make a simple script for it which asks you for the tweet and displays if successful or not

    #!/bin/sh
    echo Post your tweet.......
    read tweet
    `/usr/bin/curl -u <username>:<password> -d status="$tweet" http://twitter.com/statuses/update.xml`
    if [[ "$?" == 0 ]];
    then
    echo Updated successfuly!!!!
    exit 0
    else
    echo Something went wrong try again!!!!
    exit 1
    fi

to make it just login as root by 'sudo -i' or 'su' and type `gedit /usr/local/bin/twit` now paste the script and replace `<username>` and `<password>` with username and password of your twitter account and save the file, we will change the permissions for the file and make it  executable by typing `chmod +x /usr/local/bin/twit` all done now when you want to twit just type twit on command line and let the world know what you are doing.

PS:- if you are on twitter feel free to add me [http://twitter.com/ankur](http://twitter.com/ankur)
