from django.shortcuts import render
from django.http import HttpResponse
from .models import Advistments
# Create your views here.


def index(request):
    adv_list = Advistments.objects.all()
    return render(request,'advist/index.html', {'adv_list' : adv_list})
#створена модель та головна сторінка із використанням джинджи