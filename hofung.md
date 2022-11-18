---
layout: page
title: China
---

<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->
<h1 class="page-title">The History of Capitalism and China</h1>


<section class="recent-posts">
<div class="section-title mt-2">
    <h6 style="color: #B2B2B2; font-weight:normal" >A two-part interview with sociologist Ho-fung Hung on Chinese political economic history from the 18th century to 2008.</h6>
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
