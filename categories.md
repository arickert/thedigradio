---
layout: default
title: Categories
---


<div id="archives">
{% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/category/{{category_name| slugify}}"  class="category-head">{{ category_name }}
{% endfor %}
