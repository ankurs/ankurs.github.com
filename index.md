---
layout: page
title: Life Universe and Everything!
tagline: Supporting tagline
---
{% include JB/setup %}

{% assign first_post = site.posts.first%}                                                                                                                                                                  

# Latest - {{ first_post.title }} #

{{ first_post.content | truncatewords: 250 }}

[Read More &raquo;]({{ first_post.url}})


