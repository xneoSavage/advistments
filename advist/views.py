from django.shortcuts import render
from django.http import HttpResponse
from .models import Advistments, Rubric
# Create your views here.


def index(request):
    adv_list = Advistments.objects.all()
    rubrics = Rubric.objects.all()
    return render(request,'advist/index.html', {'adv_list' : adv_list,
                                                'rubrics' : rubrics})

def by_rubric(request, rubric_id):
    adv_list = Advistments.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'adv_list' : adv_list, 'rubrics' : rubrics,
               'current_rubric' : current_rubric}
    return render(request, 'advist/by_rubric.html', context)
#створена модель та головна сторінка із використанням джинджи
#створена модель рубрик, шаблон, урл та контроллео, преглянути це все ще раз