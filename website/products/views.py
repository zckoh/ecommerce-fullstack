from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product
from django.conf import settings


def products(request):
    return render(request, "products/products.html")


class ProductPageView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_link'] = "?Product%5BrefinementList%5D%5Bproduct_category%5D%5B0%5D="

        context['extra_images'] = []

        if context['object'].addtional_image_1:
            context['extra_images'].append(context['object'].addtional_image_1.url)
        if context['object'].addtional_image_2:
            context['extra_images'].append(context['object'].addtional_image_2.url)
        if context['object'].addtional_image_3:
            context['extra_images'].append(context['object'].addtional_image_3.url)
        if context['object'].addtional_image_4:
            context['extra_images'].append(context['object'].addtional_image_4.url)
        if context['object'].addtional_image_5:
            context['extra_images'].append(context['object'].addtional_image_5.url)

        context['product_details'] = context['object'].product_details.splitlines()

        return context
