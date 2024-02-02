from django.urls import path
from user_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('products', products, name='products'),
    path('projects', projects, name='projects'),
    path('contact', contact, name='contact'),
]