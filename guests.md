---
layout: page
title: Guests
order: 4
---
<!-- <h1 class="page-title">{{ page.title }}</h1> -->

<div style="flex-direction: column; flex-wrap: wrap; display: flex; "
  id="archives" class="guestbox">
{% assign sortedPosts = site.tags | sort %}
<div style="flex: 1 0 auto; height: 20px; width:300px; padding-bottom:2rem; color:#78C0A0">  A  </div> 
{% for tag in sortedPosts %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    {% if old_name != null %}
        {% assign old = old_name | slice: 0 %}
        {% assign new = tag_name | slice: 0 %}
        {% if old != new  %}
            <div style="padding-bottom:1.5rem; flex: 1 0 auto; height: 20px; width:330px; color: #78C0A0"> {{ new }} </div>
        {% endif %}
    {% endif %}
    <div style="padding-bottom:1.5rem;flex: 1 0 auto; font-size: 0.75rem; height: 20px; width:330px; color: #B2B2B2"> <a alt="{{ tag_name }}" style="color: #B2B2B2" href='{{site.baseurl}}/tag/{{tag_name | slugify: "ascii"}}'  class="tag-head">{{ tag_name }} </a></div>
    {% capture old_name %}{{ tag | first }}{% endcapture %}

{% endfor %}
