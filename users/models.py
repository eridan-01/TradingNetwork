from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите ваше имя",
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
    )

    email = models.EmailField(unique=True, verbose_name="Email")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
