---
layout: page
title: Newsletter
order: 5
---

<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->

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
