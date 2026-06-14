---
layout: page
title: Series
order: 6
---

<!-- <div id="archives">
{% for tag in site.tags %}
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <p></p>
    <a href="{{ site.baseurl }}/tag/{{tag_name| slugify}}"  class="tag-head">{{ tag_name }}
{% endfor %}


<!-- Begin List Posts
================================================== -->

<h1 class="page-title">{{ page.title }}</h1>

<section class="recent-posts">
<div class="row listrecent">
<ul style="color: #515151; padding-left:25px">
{% assign series = "Thawra,Iran,Antibody,The Dig Presents," | split: ',' %}
<h2 style="color:#78C0A0">Central America</h2>
<ul style="color:#515151; padding-left:25px" >
<li><a href="https://thedigradio.com/podcast/crypto-dystopia-or-popular-democracy-w-hilary-goodfriend-jorge-cuellar/" style="color: #B2B2B2">Crypto Dystopia or Popular Democracy? w/ Hilary Goodfriend & Jorge Cuéllar</a></li>
<li><a href="https://thedigradio.com/podcast/neoliberalism-violence-migration-w-hilary-goodfriend-jorge-cuellar//" style="color: #B2B2B2">Neoliberalism, Violence, and Migration w/ Hilary Goodfriend & Jorge Cuéllar</a></li>
<li><a href="https://thedigradio.com/podcast/oligarchy-empire-revolution-w-hilary-goodfriend-jorge-cuellar/" style="color: #B2B2B2">Oligarchy, Empire, Revolution w/ Hilary Goodfriend & Jorge Cuéllar</a></li>
</ul>
<h2 style="color:#78C0A0">Nusantara</h2>
<ul style="color:#515151; padding-left:25px">
<li><a href="https://thedigradio.com/podcast/nusantara-ep-1-the-long-arc-of-dutch-colonialism/" style="color: #B2B2B2">The Long Arc of Dutch Colonialism</a></li>
<li><a href="https://thedigradio.com/podcast/nusantara-ep-2-national-awakening-red-movement/" style="color: #B2B2B2">National Awakening, Red Movement</a></li>
<li><a href="https://thedigradio.com/podcast/nusantara-ep-3-japanese-occupation-indonesian-revolution/" style="color: #B2B2B2">Japanese Occupation, Indonesian Revolution</a></li>
<li><a href="https://thedigradio.com/podcast/nusantara-ep-4-indonesian-republic-third-world-revolution/" style="color: #B2B2B2">Indonesian Republic, Third World Revolution</a></li>
<li><a href="https://thedigradio.com/podcast/nusantara-ep-5-armed-conflicts-guided-democracy/" style="color: #B2B2B2">Armed Conflicts, Guided Democracy</a></li>
</ul>
{% for newpage in site.pages %}
{% if series contains newpage.title %}
    <h2 style="color:#78C0A0" >
      <a href="{{newpage.url}}">{{ newpage.title }}</a>
    </h2>
    <ul style="color:#515151; padding-left:25px" >
    {% for post in site.posts %}
      {% if post.title contains newpage.title %}
        {% unless post.title contains "Transcript" %}
            {% unless post.title contains "Newsletter" %}
                {% unless post.title contains "Isabella" %}

                <li><a href="{{ post.url }}" style="color: #B2B2B2" >{{ post.title }}</a></li>
                {% endunless %}

            {% endunless %}
        {% endunless %}
      {% endif %}
    {% endfor %}
    </ul>
{% endif %}
{% endfor %}
</ul>
</div>
</section>
