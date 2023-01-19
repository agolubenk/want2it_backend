from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('index', views.menu_list, name='menu_list'),
    path('home', views.menu_list, name='menu_list'),
    path('404', views.error_404_page, name='error_404_page'),
]

handler404 = "start.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)