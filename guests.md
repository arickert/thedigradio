---
layout: default
title: Tag
---

<div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}
