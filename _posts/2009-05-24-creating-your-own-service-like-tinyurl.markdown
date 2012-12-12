---
comments: true
date: 2009-05-24 15:15:56
layout: post
slug: creating-your-own-service-like-tinyurl
title: Creating your own service like tinyurl
wordpress_id: 505
---

Few weeks ago i came across [this](http://www.techcrunch.com/2009/03/30/if-bitly-is-worth-8-million-tinyurl-is-worth-at-least-46-million/) article on Techcrunch which says tinyurl is worth $46Million (of course before twitter started using bit.ly as default) which made me think how hard is it to make a simple service like tinyurl and i figured out its not hard. 

so i used apache's mod\_rewrite to rewrite the url and forward the code to a php script ( url.php ) which will then search for the url in database and take the use to the original url and for shorting, url it is inserted into a table with a auto increment primary key and the key is converted to base36 which contains `[a-z]` and `[0-9]`, making the short code...

First create a database say 'shorturl'

    CREATE TABLE IF NOT EXISTS `shorturl` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `url` varchar(300) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

then create file .htaccess where you want your url to be and write

    RewriteEngine On
    RewriteCond %{REQUEST_URI} \/([0-9a-z]*)$ [NC]
    RewriteRule ^(.*) url.php?url=%1 [L]

and to create the url we will use a simple file say create.php

    <html>
    <head>
    <title>Url Shortner</title>
    </head>
    <body>
        <?php
            ob_start();
            $host=""; //host
            $dbuser=""; // database username
            $dbpass=""; // database password
            $db=""; //database name
            $con = mysql_connect($host,$dbuser,$dbpass);
            mysql_select_db("url",$con);
            if (!isset($_POST['shorten']))
            {
                echo "<center><h3>Enter the url to shorten</h3><form method='POST'><input type='text' name='url' />
                <input type='submit' name='shorten' value='Shorten' /></form></center>";
            }
            else
            {
                if (isset($_POST['url']))
                {
                    $url=" ".mysql_real_escape_string($_POST['url']);
                    if (strpos($url,"http://") or strpos($url,"https://") or strpos($url,"ftp://"))
                    {
                        $url=mysql_real_escape_string($_POST['url']);
                    }
                    else
                    {
                        $url="http://".mysql_real_escape_string($_POST['url']);
                    }
                    $q="select * from url where url='{$url}'";
                    $res = mysql_query($q,$con);
                    $row=mysql_fetch_row($res);
                    if (!$row)
                    {
                        $query="insert into url set url='{$url}'";
                        $res = mysql_query($query,$con);
                    }
                    $query1="select id from url where url='{$url}' limit 1";
                    $res=mysql_query($query1,$con);
                    $row=mysql_fetch_row($res);
                    echo "shortened url is http://yoursite.com/".base_convert($row[0],10,36);
                }
            }
            ob_end_flush();
        ?>
    </body>
    </html>

then our url.php file

    <?php
    ob_start();
    $host=""; //host
    $dbuser=""; // database username
    $dbpass=""; // database password
    $db=""; //database name
    $con = mysql_connect($host,$dbuser,$dbpass);
    mysql_select_db($db,$con);
    if (isset($_GET['url']))
    {
        $query="select * from url where id ='".base_convert(mysql_real_escape_string($_GET['url']),36,10)."'";
        $res = mysql_query($query,$con);
        $row=mysql_fetch_row($res);
        header("Location: ".$row[1]);
    }
    ob_end_flush();
    ?>


Download [here](http://ankurs.com/wp-content/uploads/2009/05/urltar.gz)
