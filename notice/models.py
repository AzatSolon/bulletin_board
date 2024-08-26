from django.db import models


class Ad(models.Model):
    """
    Объявление
    """

    title = models.CharField(
        unique=True, max_length=100, verbose_name="название товара"
    )
    price = models.PositiveIntegerField(verbose_name="цена товара")
    description = models.TextField(max_length=200, verbose_name="описание товара")
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        max_length=100,
        verbose_name="автор объявления",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="время и дата создания объявления"
    )
    image = models.ImageField(upload_to="ad_images", null=True, blank=True)


class Comment(models.Model):
    """
    Отзыв
    """

    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Mymodel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
