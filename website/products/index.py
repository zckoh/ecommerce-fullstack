from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = ('product_name', 'model_no', 'product_category',
            'product_details', 'slug', 'main_product_image')
