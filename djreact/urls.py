
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('api-auth/', include('rest_framework.urls')),
     path('admin/', admin.site.urls),
     path('api/',include('articles.api.urls')),
      path('pos/',include('articles.posters.urls')),
      path('trailers/',include('articles.trailers.urls')),
      path('cast/',include('articles.Cast.urls')),

]

urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)