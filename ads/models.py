# Create your models here.
import datetime
from users.models import User
from django.db import models

class Selection(models.Model): # 30-06 ...
    name = models.CharField(max_length=20, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    list_of_ad = models.ManyToManyField(Ad)
    class Meta:
        verbose_name = "Выборка"
        verbose_name_plural = "Выборки"
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name


class Ad(models.Model):
    STATUS = [
        ("true", "опубликовано"),
        ("false", "не опубликовано")
    ]
    name = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # _id:try ADD
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    is_published = models.CharField(max_length=5, choices=STATUS, default="false")
    image = models.ImageField(upload_to="ads/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # _id:try ADD
    #created = models.DateField(default=datetime.date.today) # try ADD

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
    def __str__(self):
        return self.name

    # 22-06
    @property
    def username(self):
        return self.author.username if self.author else None

