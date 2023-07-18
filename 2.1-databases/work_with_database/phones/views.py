from django.shortcuts import render, redirect
from .models import Phone
from django.shortcuts import get_object_or_404


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    phone = Phone.objects.all()

    match sort:
        case 'name':
            sort_by = 'name'
        case 'max_price':
            sort_by = '-price'
        case 'min_price':
            sort_by = 'price'
        case _:
            sort_by = None
    
    if sort:
        phone = phone.order_by(sort_by)
    
    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': get_object_or_404(Phone, slug=slug)
    }
    return render(request, template, context)
