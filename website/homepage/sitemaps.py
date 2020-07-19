from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class HomepageSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return ['homepage_view']

    def location(self, item):
        return reverse(item)