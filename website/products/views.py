from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ProductPage(TemplateView):
    template_name = "products/product_page.html"

class CataloguePage(TemplateView):
    template_name = "products/product_catalogue.html"

def products(request):
    return render(request, "products/products.html")