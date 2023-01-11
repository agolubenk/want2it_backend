from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include




urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('about/', views.PostListAbout.as_view(), name='about'),
    path('vacancy/', views.PostListVacancy.as_view(), name='vacancy'),
    path('docs/', views.PostListDocs.as_view(), name='docs'),
    path('join/', views.PostListJoin.as_view(), name='join'),
    path('upload/', views.PostListUpload.as_view(), name='upload'),
    path('invite/', views.PostListInvite.as_view(), name='invite'),
    path('', views.PostListHome.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'blog.views.error_404_view'




