from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.contact_view, name="contact_view"),
    path("thanks", views.thankyou_view, name="thankyou_view"),
]