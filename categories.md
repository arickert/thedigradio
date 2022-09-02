---
layout: page
title: Topics
---

<h1 class="page-title">{{ page.title }}</h1>

<div style="width:100%; text-align:justify" id="archives">

{% assign sortedPosts = site.categories | sort %}
{% for category in sortedPosts %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    {% unless category_name == "archive" %}
        <a style="color:#B2B2B2; font-size:0.8rem" href="{{ site.baseurl }}/category/{{category_name| slugify}}" class="category-head1">{{ category_name }} </a>
        <span style="color:#515151; font-size:0.8rem">&#8226;</span>
    {% endunless %}
{% endfor %}
