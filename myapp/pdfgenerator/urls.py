from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data", views.get_data, name="get_data"),
    path("pdf/", views.generate_pdf, name="generate_pdf"),
    path("pdf2/", views.generate_pdf2, name="generate_pdf2"),
]
