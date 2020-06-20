from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Product

class ProductSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return ['products']

    def location(self, item):
        return reverse(item)

class AllProductsSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return Product.objects.all()
    