from django.urls import path
from . import views, models
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path(
        "toys",
        views.CataloguePage.as_view(
            extra_context={
                "category_name": "Toys",
                "category_catalogue": "toys_catalogue",
                "category_fullname": "Toys/Jouets",
                "category_description": "We have toys from LEGO, Hot Wheels, Drones, Remote Controlled Racing Cars, Barbie dolls and many more.",
                "header_background_image": "catalogue/toys-header.jpg",
                "products": models.toys_product_list()
            }
        ),
        name="toys_catalogue"
    ),

    path(
        "copybooks",
        views.CataloguePage.as_view(
            extra_context={
                "category_name": "Copybooks",
                "category_catalogue": "copybooks_catalogue",
                "category_fullname": "Copybooks/Cahiers",
                "category_description": "We have copybooks from Rhodia, Baron, Whitelines, Pilot, etc",
                "header_background_image": "catalogue/copybooks-header.jpg",
                "products": models.copybooks_product_list()
            }
        ),
        name="copybooks_catalogue"
    ),

    path(
        "pens",
        views.CataloguePage.as_view(
            extra_context={
                "category_name": "Pens",
                "category_catalogue": "pens_catalogue",
                "category_fullname": "Pens/Plumes",
                "category_description": "We have pens from Stabilo, Pilo, Pentel, Staedtler, etc",
                "header_background_image": "catalogue/pens-header.jpg",
                "products": models.pens_product_list()
            }
        ),
        name="pens_catalogue"
    ),
]

# Add additional urls for each product
for id, product in models.toys_product_list().items():
    route = path(
        'toys/{}.html'.format(product['url_name']),
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)

for id, product in models.copybooks_product_list().items():
    route = path(
        'copybooks/{}.html'.format(product['url_name']),
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)

for id, product in models.pens_product_list().items():
    route = path(
        'pens/{}.html'.format(product['url_name']),
        views.ProductPage.as_view(extra_context=product),
        name=product['url_name'],
    )
    urlpatterns.append(route)
