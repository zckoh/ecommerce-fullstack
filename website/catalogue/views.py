from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ProductPage(TemplateView):
    template_name = "catalogue/product_page.html"

class CataloguePage(TemplateView):
    template_name = "catalogue/product_catalogue.html"

def test_search(request):
    return render(request, "catalogue/test_search.html")

def catalogue(request):
    return render(request, "catalogue/catalogue.html")