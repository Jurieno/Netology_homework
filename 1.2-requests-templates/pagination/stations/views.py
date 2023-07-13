from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request): 
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    current_page = request.GET.get('page', 1)
    context = {}

    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        paginator = Paginator(list(reader), 10)
        page = paginator.get_page(current_page)

        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
        
    return render(request, 'stations/index.html', context)

