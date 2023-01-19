from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import start


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('start.urls')),
    path('', include('vacancy.urls')),
    path('', include('orders.urls')),
    path('', include('accounting.urls')),
    path('summernote/', include('django_summernote.urls')),

]

handler404 = "start.views.page_not_found_view"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)