from django.urls import path
from . import views, models
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path("", views.catalogue, name="catalogue")
]

# Add additional urls for each product
for product in models.toys_product_list():
    route = path(
        product['url_link'],
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)

for product in models.copybooks_product_list():
    route = path(
        product['url_link'],
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)

for product in models.pens_product_list():
    route = path(
        product['url_link'],
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)
