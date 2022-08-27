from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from filmophile import settings
from films.views import FilmViewSet

film_router = routers.DefaultRouter()
film_router.register(r'films', FilmViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(film_router.urls)),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
