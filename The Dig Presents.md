---
layout: page2
title: The Dig Presents
---

<div style="background-image: url(/assets/Blacklinework.png);         background-size: cover">
<!-- <h1 class="page-title">The Dig Presents</h1> -->
<img src="/assets/croptext.png">

<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: white; font-weight:normal" >

<p>
The Dig Presents is a monthly series that features original documentary reporting, personal narrative, and other sonic experiments from a wide range of contributors.
</p>
<p>
Produced and edited by Liza Yeager and Mitchell Johnson.
</p>
<p>
If you’re interested in pitching a story to The Dig Presents, email thedigpresents@gmail.com. </p> </h6>
</div>
<div class="row listrecent">
{% for post in site.posts %}
{% if post.title contains "The Dig Presents" %}
    {% if post.title contains "Newsletter" %}
    {% else %}
    {% include postbox2.md %}
    {% endif %}
{% endif %}

{% endfor %}
</div>
</section>
</div>
