from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserRoles, UserManager

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=25, verbose_name="имя пользователя")
    last_name = models.CharField(max_length=40, verbose_name="фамилия пользователя")
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    image = models.ImageField(
        upload_to="users/avatars", verbose_name="аватар", **NULLABLE
    )
    role = models.CharField(
        max_length=3, choices=UserRoles.choices, default=UserRoles.USER
    )
    is_active = models.BooleanField(default=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = "email"

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return f"{self.email},{self.phone}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
