from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from .forms import OrderForm
from .models import Order
from telebot.sendmessage import sendTelegram

# Create your views here.

def index(request):
    slider_list = CmsSlider.objects.all()

    price1 = PriceCard.objects.get(pk=1)
    price2 = PriceCard.objects.get(pk=2)
    price3 = PriceCard.objects.get(pk=3)

    price_table = PriceTable.objects.all()
    form = OrderForm()
    context = {'slider_list': slider_list,
               'price1': price1,
               'price2': price2,
               'price3': price3,
               'price_table': price_table,
               'form': form,
               }
    return render(request, 'crm/index.html', context)


def thanks_page(request):
    if not request.POST:
        raise Http404()
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    element = Order(name=name, email=email, order_phone=phone)
    element.save()
    sendTelegram(name=name, email=email, order_phone=phone)

    return render(request, 'crm/thanks.html', {'name': name})


