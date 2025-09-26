from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=20)
    surname = models.CharField("Фамилия", max_length=25)
    birthday = models.DateField("Дата рождения")
    bio = models.TextField("Биография")
    desc = models.CharField("Жив или нежив", default="Умер")

    class Meta:
        verbose_name  = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["surname", "bio"],
                condition=models.Q(desc="Жив"),
                name = "unique_surname_bio"
            ),
        ]

    def __str__(self):
        return f"{self.surname} {self.name}"


class Publisher(models.Model):
    name = models.CharField("Название", unique=True)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_author = models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.title}"
