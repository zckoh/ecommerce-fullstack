from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import models

# Create your views here.
class ProductPage(TemplateView):
    template_name = "catalogue/product_page.html"

class CataloguePage(TemplateView):
    template_name = "catalogue/product_catalogue.html"
