
from django.contrib import admin
from django.urls import path,include,re_path
from articles.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path('admin/1/', admin.site.urls),
      re_path('(?P<path>.*)/$', index, name='index'),
      path('',index,name="index"),
      path('api-auth/', include('rest_framework.urls')),
      path('api',include('articles.api.urls')),
      path('pos/',include('articles.posters.urls')),
      path('trailers/',include('articles.trailers.urls')),
      path('cast',include('articles.Cast.urls')),
      


]

urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)