
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Event


def details(request, id):
    event = get_object_or_404(Event, id=id),
    return render(request, 'events/details.html')


def list(request):
    

    filter_map = {
        'query': 'name__icontains',
        'category': 'category__exact',
        'price_min': 'price__gte',
        'price_max': 'price__lte'
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value

    events = Event.objects.filter(**filters)

    context = {
        "events": events
    }     

    today = datetime.today()

    events = Event.objects.filter(
        datetime__gte=today).order_by("datetime")
    return render(request, 'events/list.html', {"events": events})
