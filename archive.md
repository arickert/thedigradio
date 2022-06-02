---
layout: page
title: Episodes
---

{% assign postsByYearMonth = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}
{% for yearMonth in postsByYearMonth %}
  <h2 style="color:#82BFAE" >{{ yearMonth.name }}</h2>
  <ul style="color:#515151; padding-left:25px" >
    {% for post in yearMonth.items %}
      {% unless post.title contains "Newsletter" or post.title contains "Transcript" %}
        <li><a href="{{ post.url }}" style="color: #B2B2B2" >{{ post.title }}</a></li>
      {% endunless %}
    {% endfor %}
  </ul>
{% endfor %}
