from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item
# Create your views here.


def get_session(request, pk):
    return HttpResponse('sdasjkdjl;as')


def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'stripe_simple/buy_item.html', context)