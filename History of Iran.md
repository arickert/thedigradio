---
layout: page
title: Iran
---


<h1 class="page-title">History of Modern Iran</h1>

<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: #B2B2B2; font-weight:normal" >A four part series featuring Eskandar Sadeghi-Boroujerdi and Golnar Nikpour on the history of modern Iran. </h6>
</div>
<div class="row listrecent">
<ul style="color: #515151; padding-left:25px">
{% for post in site.posts %}
{% if post.title contains page.title %}
    {% if post.title contains "Newsletter" %}
    {% else %}
    <li style="margin-bottom:0.5rem">
    <a style="color: #B2B2B2" href="{{post.url}}">{{post.title}}</a>
    </li>
    {% endif %}
{% endif %}    

{% endfor %}
</ul>
</div>
</section>
