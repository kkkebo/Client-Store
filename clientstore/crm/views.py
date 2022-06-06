from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from cms.models import CmsSlider
from .models import Order


# Create your views here.

def index(request):
    slider_list = CmsSlider.objects.all()
    context = {'slider_list': slider_list}
    return render(request, 'crm/index.html', context)

def thanks_page(request):
    return render(request, 'crm/thanks_page.html')


