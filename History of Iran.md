---
layout: page
title: Iran
---


<h1 class="page-title">History of Modern Iran</h1>

<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: #B2B2B2; font-weight:normal" >A five part series featuring Eskandar Sadeghi-Boroujerdi and Golnar Nikpour on the history of modern Iran. </h6>
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
