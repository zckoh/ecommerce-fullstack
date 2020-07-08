"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from products import models


urlpatterns = [
    path('', include('homepage.urls')),
    path('contact/', include('contact.urls')),
    path('products/', include('products.urls')),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", 
        content_type="text/plain")
    ),
    path('sitemap.xml', TemplateView.as_view(
        template_name="sitemap.xml", 
        content_type="application/xml"), 
        {'products': models.get_product_list()}
    )
    # path('about/', include('about.urls')),
]
