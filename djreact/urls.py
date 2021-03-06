
from django.contrib import admin
from django.urls import path, include, re_path
from articles.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api', include('articles.api.urls')),
    path('pos', include('articles.posters.urls')),
    path('trailers', include('articles.trailers.urls')),
    path('cast', include('articles.Cast.urls')),
    path('articalAssets', include('articles.articalAssets.urls')),
    path('webseries', include('articles.webSeries.urls'))




]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
