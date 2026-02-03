"""
URL configuration for HRMS_lite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HRMS.urls')),
]

# Custom error handlers
handler404 = 'HRMS.views.custom_404'
handler500 = 'HRMS.views.custom_500'
