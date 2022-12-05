from django.contrib import admin

# Register your models here.
from .models import Student # импортируем модель Student

admin.site.register(Student) # регистрируем модель Student