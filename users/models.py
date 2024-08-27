from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель Пользователя"""

    USER = "user"
    ADMIN = "admin"

    ROLE_CHOICES = [
        (USER, "User"),
        (ADMIN, "Admin"),
    ]
    username = None
    first_name = models.CharField(max_length=45, verbose_name="Имя", **NULLABLE)
    last_name = models.CharField(max_length=60, verbose_name="фамилия", **NULLABLE)
    phone = models.CharField(max_length=22, verbose_name="телефон", **NULLABLE)
    email = models.EmailField(unique=True, verbose_name="email")
    role = models.CharField(choices=ROLE_CHOICES, default=USER)
    image = models.ImageField(upload_to="images/", verbose_name="аватар", **NULLABLE)
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
