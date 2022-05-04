---
layout: page
title: Guests
---
<h1 class="page-title">{{ page.title }}</h1>

<div id="archives">
{% assign sortedPosts = site.tags | sort %}
{% for tag in sortedPosts %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{site.baseurl}}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}
