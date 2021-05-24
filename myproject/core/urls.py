from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contacto/', views.contact, name='contact'),
    url('hacemos/', TemplateView.as_view(template_name="hacemos.html")),
    path('hacemos/', views.hacemos, name='hacemos'),
]

