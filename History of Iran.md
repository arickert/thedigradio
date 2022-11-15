---
layout: page
title: Iran
---


<h1 class="page-title">{{ page.title }}</h1>

<section class="recent-posts">
<div class="row listrecent">
<ul style="color: #515151; padding-left:25px">
{% for post in site.posts %}
{% if post.title contains page.title %}
    <li style="margin-bottom:0.5rem">
    <a style="color: #B2B2B2" href="{{post.url}}">{{post.title}}</a>
    </li>
{% endif %}    

{% endfor %}
</ul>
</div>
</section>
