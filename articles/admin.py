from django.contrib import admin
from .models import Movie,Poster,Trailer,Cast

admin.site.register(Poster)
admin.site.register(Movie)
admin.site.register(Trailer)
admin.site.register(Cast)