---
layout: page
title: Central America
---

<h1 class="page-title">Central America</h1>

<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: #B2B2B2; font-weight:normal">
        A Dig series on late-19th and early-20th century Central America.
    </h6>
</div>
<div class="row listrecent">
{% for post in site.posts %}
{% if post.title contains page.title %}
    {% if post.title contains "Newsletter" %}
    {% else %}
    {% include postbox.md %}
    {% endif %}
{% endif %}
{% endfor %}
</div>
</section>
