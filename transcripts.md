---
layout: page
title: Transcript
---

<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->


<section class="recent-posts">
<!-- <div class="section-title mt-2">
    <h2>Transcripts</h2>
</div> -->
<div class="row listrecent">

{% for post in site.posts %}
{% if post.title contains page.title %}
    {% include postbox.md %}
{% endif %}    

{% endfor %}

</div>
</section>