---
layout: page
title: Topics
order: 3
---

<h1 class="page-title">{{ page.title }}</h1>

<div style="width:100%; text-align:justify" id="archives">

{% assign sortedPosts = site.categories | sort %}
{% for category in sortedPosts %}
    {% unless category contains "Archive" %}
        {% capture category_name %}{{ category | first }}{% endcapture %}
            <a alt="{{ category_name }}" style="color:#B2B2B2; font-size:0.8rem" href='{{ site.baseurl }}/category/{{category_name| slugify: "ascii" }}' class="category-head1">{{ category_name }} </a>
            <span style="color:#515151; font-size:0.8rem">&#8226;</span>
    {% endunless %}
{% endfor %}
