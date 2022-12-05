from django.db import models

# Create your models here.
class Student(models.Model): # создали модель (таблицу)
    name=models.CharField(max_length=100) # тут описываем столбцы.
                                          # CharField - строковый тип данных
                                          # max_length - максимальная длина
                                        # blank=False - указываем, что не может быть пустым
    des=models.TextField()
    def __str__(self): # это метод, который позвоняет переименовать название строк в админке Джанго
        return self.name # переименовываем на фамилию