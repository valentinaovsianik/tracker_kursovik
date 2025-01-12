from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="укажите email",
        blank=False,
        null=False,
    )

    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True, help_text="укажите телефон")

    tg_nik = models.CharField(
        max_length=50,
        verbose_name="TG",
        help_text="Укажите TG-ник",
        blank=True,
        null=True,
        default="default_tg_nik",
    )

    avatar = models.ImageField(
        upload_to="avatars/", verbose_name="Аватарка", blank=True, null=True, help_text="добавьте аватарку"
    )

    tg_chat_id = models.CharField(
        max_length=50, null=True, blank=True, default="", verbose_name="TG chat_id", help_text="укажите TG chat_id"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
