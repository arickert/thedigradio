---
layout: page
title: Thawra
---


<h1 class="page-title">Thawra</h1>

<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: #B2B2B2; font-weight:normal" >Our rolling mini-series on Arab radicalisms in the 20th century. Listen to Thawra through our website or wherever you get your podcasts, and don't forget to rate and review! </h6>
<a href="https://podcasts.apple.com/us/podcast/thawra/id1761860819"><i class="fa-brands fa-apple" style="color:#B2B2B2; font-size:30px; padding-left:5px;"></i></a>
<a href="https://open.spotify.com/show/0e0eE7aKt5EQdg07CzeVoI?si=LoX8DixhRH6HN6sScejGWw"><i class="fa-brands fa-spotify" style="color:#B2B2B2; font-size:30px; padding-left:5px;"></i></a>
</div>
<div class="row listrecent">
{% for post in site.posts reversed %}
{% if post.title contains page.title %}
      {% if post.title contains "Newsletter" %}
    {% else %}
    {% include postbox.md %}
    {% endif %}
{% endif %}

{% endfor %}
</div>
</section>
