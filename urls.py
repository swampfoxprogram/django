The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/


from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import  settings 
from import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
