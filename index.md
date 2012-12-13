---
layout: page
title: Recent Posts
tagline: 
---
{% include JB/setup %}

{% assign first_post = site.posts.first %}                                                                                                                                                                  

{% for post in site.posts %}
    {% if forloop.index < 5 %}
#[{{ post.title }}] ({{ post.url}})# 
Published:
<span class="month"><abbr>{{ post.date | date: '%B' }}</abbr></span>
<span class="day">{{ post.date | date: '%d' }}</span>
<span class="year">{{ post.date | date: '%Y' }}</span>


{{ post.content | truncatewords: 250 }}

[Read More &raquo;]({{ post.url}})
    {% endif %}
{% endfor %}

-----------------------------------

### [See All Posts](/archive.html) ###
