---
comments: true
date: 2008-04-09 09:28:27
layout: post
slug: automatic-login-and-pop-up-block-on-i-on
title: Automatic Login and pop-up block on I-ON
wordpress_id: 357
---

Are you sick of the same I-ON login page that asks you to enable pop-ups every time you open your browser and try to access the Internet, are you sick of entering your username and password again and again. I think i have a very very simple solution for all your problems. Just copy the below code and save it as any name say ankur.html and just make it homepage of your browser and dont forget to replace "your username" and "your password" to the actual one you are using, now whenever you open your  browser TaDa you are all set to go and one more thing if you dont want the pop-up you can just disable them no need to enable them
Copy from here

    <script type="text/javascript">
    function login()
    {
        document.loginframe.submit();
    }
    </script>
    <body onload="login()" >
        <form name="loginframe" method="post" action="http://192.168.150.2:8080/clntAuth/clntAuth_main.jsp">
            <input type="submit" value="Sign In" >
            <input type="hidden" name="loginID"  value="your username">
            <input type="hidden" name="loginpassword"  value="your password">
            <input type="hidden" name="flag" value="0">
            <input type="hidden" name="popcheck" value="0">
        </form>
    </body>


This is a very simple method you can understand it just by reading the above code, i knew this method from a long time but have posted it now because of a recent event anyway dont forget to replace "your username" and "your password" to the actual one you are using
Happy Surfing!!!!!

PS - I will really be happy to hear if it helps you or not...........

