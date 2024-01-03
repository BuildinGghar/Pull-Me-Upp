from django.shortcuts import render

# Create your views here.


def index(request):
    # Filter services for WOMEN, MEN, and KIDS
    women_services = Service.objects.filter(service_type=Service.WOMEN)[:5]
    men_services = Service.objects.filter(service_type=Service.MEN)[:5]
    kids_services = Service.objects.filter(service_type=Service.KIDS)[:5]

    context = {
        'women_services': women_services,
        'men_services': men_services,
        'kids_services': kids_services,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Service

from django.shortcuts import render
from .models import Service

def price(request):
    # Filter services for WOMEN, MEN, and KIDS
    women_services = Service.objects.filter(service_type=Service.WOMEN)
    men_services = Service.objects.filter(service_type=Service.MEN)
    kids_services = Service.objects.filter(service_type=Service.KIDS)

    context = {
        'women_services': women_services,
        'men_services': men_services,
        'kids_services': kids_services,
    }

    return render(request, 'price.html', context)
