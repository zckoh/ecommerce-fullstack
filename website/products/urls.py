from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path('<slug:slug>', views.ProductPageView.as_view(), name='product_page'),
]
