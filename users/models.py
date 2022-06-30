from django.db import models
from django.contrib.auth.models import AbstractUser # 30-06 ...

class Location(models.Model):
    name = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name

#class User(models.Model):
class User(AbstractUser):# 30-06 ...
    MEMBER = "member"
    MODERATOR ="moderator"
    ADMIN = "admin" # ... 30-06
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=20, db_index=True, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=9, choices=ROLES, default="member")
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
