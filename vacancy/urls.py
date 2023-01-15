from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('vacancy/', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('мфсфтсн/', views.vacancy_list, name='vacancy_list'),
    path('мфсфтсн/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('вакансии/', views.vacancy_list, name='vacancy_list'),
    path('вакансии/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)