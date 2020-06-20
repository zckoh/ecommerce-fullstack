from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from homepage.sitemaps import HomepageSitemap
from contact.sitemaps import ContactSitemap
from products.sitemaps import ProductSitemap, AllProductsSitemap
from django.contrib.sitemaps.views import sitemap

admin.site.site_header = 'Brand Name Website Administration'
admin.site.index_title = 'Administration Page'
admin.site.site_title = 'Brand Name Website Administration'


sitemaps = {
    'homepage' : HomepageSitemap,
    'contact' : ContactSitemap,
    'product' : ProductSitemap,
    'all_product' : AllProductsSitemap,
}

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('products/', include('products.urls')),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", 
        content_type="text/plain")
    ),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}),
]
