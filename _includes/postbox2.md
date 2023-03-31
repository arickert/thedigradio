{% assign showFeaturedImage = include.showImage | default: false %}

<div class="col-lg-4 col-md-6 mb-30px card-group">
    <div class="card h-100">
        <div class="card-body">
            <h6 class="card-title" style="margin-bottom:0 color: #white">
                <a class="text-dark" style="color:white" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
            </h6>
        </div>
    </div>
</div>