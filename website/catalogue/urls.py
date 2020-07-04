from django.urls import path
from . import views, models
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path("", views.catalogue, name="catalogue")
]

# base link to go back to catalogue with filter
category_refinement_base_link = "?products_index%5BrefinementList%5D%5Bproduct_category%5D%5B0%5D="

# Add additional urls for each product
for product in models.get_product_list():
    product.update( {"category_link" : category_refinement_base_link + product['product_category']} )
    route = path(
        product['url_link'],
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)