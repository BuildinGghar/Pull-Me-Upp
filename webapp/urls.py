from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('blog_details', blog_details, name='blog_details'),
    path('price', price, name='price'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

