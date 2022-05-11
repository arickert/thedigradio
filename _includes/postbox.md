{% assign showFeaturedImage = include.showImage | default: false %}

<div class="col-lg-4 col-md-6 mb-30px card-group">
    <div class="card h-100">
        {% if showFeaturedImage and post.image and site.data.settings.showImagesInPostbox %}
        <div class="maxthumb">
            <a href="{{ site.baseurl }}{{ post.url }}">       
                    {% if site.lazyimages == "enabled" %}
                        <img class="img-fluid lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ site.baseurl }}/{{ post.image }}{% endif %}" alt="{{ post.title }}">
                    {% else %}
                        <img class="img-fluid" src="{% if post.image contains "://" %}{{ post.image }}{% else %}{{ site.baseurl }}/{{ post.image }}{% endif %}" alt="{{ post.title }}"> 
                    {% endif %}                
            </a>
        </div>
        {% endif %}
        <div class="card-body">
            <h3 class="card-title" style="margin-bottom:0 color: #79AA9D">
                <a class="text-dark" style="color: #79AA9D" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
            </h3>
            {% unless post.title contains "Newsletter" %}
            <small class="text-muted" style="color:#515151">{{ post.date | date_to_string }}</small>
            {% endunless %}
            <br>
            <small class="card-text mt-2" style="color:#9a9a9a; font-weight:normal" >{{ post.excerpt | strip_html | truncatewords:35 }}</small>
        </div>
    </div>
</div>