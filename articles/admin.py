from django.contrib import admin
from .models import Movie, Poster, Trailer, Cast, ArticalImage, webSeries

admin.site.register(Poster)
admin.site.register(Movie)
admin.site.register(Trailer)
admin.site.register(Cast)
admin.site.register(ArticalImage)
admin.site.register(webSeries)
