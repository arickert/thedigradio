---
layout: page
title: Categories
---


<div id="archives">
{% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <a href="{{ site.baseurl }}/category/{{category_name| slugify}}"  class="category-head">{{ category_name }}
{% endfor %}
