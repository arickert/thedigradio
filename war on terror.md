---
layout: page
title: War on Terror w
---

<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->
<h1 class="page-title">War on Terror</h1>


<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: #B2B2B2; font-weight:normal" >The Dig’s War on Terror trilogy with Spencer Ackerman.</h6>
</div>
<div class="row listrecent">

{% for post in site.posts %}
{% if post.title contains page.title %}
    {% unless post.title contains "Newsletter" %}
        {% unless post.title contains "Transcript" %}
            {% include postbox.md %}
        {% endunless %}
    {% endunless %}
{% endif %}    

{% endfor %}

</div>
</section>
