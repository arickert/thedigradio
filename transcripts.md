---
layout: page
title: Transcripts
order: 7
---
<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->

{% assign postsByYearMonth = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}
{% for yearMonth in postsByYearMonth %}
  {% assign valid_posts = yearMonth.items | where_exp: "post", "post.title contains 'Newsletter' or post.title contains 'Introducing Thawra' or post.permalink contains 'podcast' or post.title contains 'Selections'" | size %}
  
  {% if valid_posts > 0 %}
    <h2 style="color:#78C0A0">{{ yearMonth.name }}</h2>
    <ul style="color:#515151; padding-left:25px">
      {% for post in yearMonth.items %}
        {% unless post.title contains "Newsletter" or post.title contains "Introducing Thawra" or post.permalink contains "podcast" or post.title contains "Selections" %}
          <li><a href="{{ post.url }}" style="color: #B2B2B2">{{ post.title }}</a></li>
        {% endunless %}
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
