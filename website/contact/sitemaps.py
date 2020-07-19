from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class ContactSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return ['contact_view', 'thankyou_view']

    def location(self, item):
        return reverse(item)