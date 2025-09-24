from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=20)
    surname = models.CharField("Фамилия", max_length=25)
    birthday = models.DateField("Дата рожденич")
    bio = models.TextField("Биография")

class Publisher(models.Model):
    name = models.CharField("Название", unique=True)

class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_author = models.ManyToManyField(Author)