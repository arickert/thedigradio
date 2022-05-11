---
layout: page
title: Transcript
---

<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->

<h1 class="page-title">{{ page.title }}s</h1>

<section class="recent-posts">
<div class="row listrecent">
<ul style="color: #515151; padding-left:25px">
{% for post in site.posts %}
{% if post.title contains page.title %}
    <li style="margin-bottom:0.5rem">
    {% assign newtitle = post.title | split: "ranscript: " %}
    {% for title in newtitle offset:1 limit:1 %}
        <a style="color: #9a9a9a" href="{{post.url}}">{{title}}</a>
    {% endfor %}
    </li>
{% endif %}    

{% endfor %}
</ul>
</div>
</section>
