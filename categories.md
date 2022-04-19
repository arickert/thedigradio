---
layout: page
title: Topics
---


<div id="archives">
{% assign sortedPosts = site.categories | sort %}
{% for category in sortedPosts %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    {% assign remainder = forloop.index | modulo: 3 %}
    {% if remainder == 0 %}
    <a href="{{ site.baseurl }}/category/{{category_name| slugify}}" style="color:red" class="category-head1">{{ category_name }}
    {% elsif remainder == 1 %}
    <a href="{{ site.baseurl }}/category/{{category_name| slugify}}" style="color:blue" class="category-head2">{{ category_name }}
    {% elsif remainder == 2 %}
    <a href="{{ site.baseurl }}/category/{{category_name| slugify}}" style="color:brown" class="category-head3">{{ category_name }}
    {% endif %}
{% endfor %}
