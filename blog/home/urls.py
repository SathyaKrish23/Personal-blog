from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =  [
    path('', views.index),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),  
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)