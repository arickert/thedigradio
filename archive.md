---
layout: page
title: Episodes
order: 1
---

{% assign postsByYearMonth = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}
{% for yearMonth in postsByYearMonth %}
  <h2 style="color:#78C0A0" >{{ yearMonth.name }}</h2>
  <ul style="color:#515151; padding-left:25px" >
    {% for post in yearMonth.items %}
      {% unless post.title contains "Newsletter" or post.title contains "Introducing Thawra" or post.title contains "Transcript" or post.title contains "Selections" %}
        <li><a href="{{ post.url }}" style="color: #B2B2B2" >{{ post.title }}</a></li>
      {% endunless %}
    {% endfor %}
  </ul>
{% endfor %}
