from django.shortcuts import render
from .models import Student # импортируем студенческую модель

# Create your views here.
def index(request):
    obj = Student.objects.all() # создаём объект для студенческой модели
    context={
        'obj':obj,
    }
    return render(request, 'index.html', context)