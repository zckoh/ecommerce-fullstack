from django.views.generic import ListView
from django.shortcuts import render
from .models import Notice

class HomePage(ListView):
    template_name = 'homepage/homepage.html'
    queryset = Notice.objects.order_by('-updated_date')[:3]
    context_object_name = 'notices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("hello")
        context['last_updated'] = Notice.objects.order_by('-updated_date').first()
        print(context['last_updated'])
        return context