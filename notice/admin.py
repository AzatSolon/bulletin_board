from django.contrib import admin

from notice.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "description", "author", "created_at")
    list_filter = ("title",)
    search_fields = ("title",)
