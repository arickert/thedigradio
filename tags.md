---
layout: default
title: Tags
---

<div id="archives">
{% for tags in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}
