from django.contrib import admin

from . import models


@admin.register(models.SessionHandler)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ("session_key", "path", "count_of_visits", "user")
    search_fields = (
        "user",
        "session_key",
        "path",
    )
    list_filter = ("user",)
    list_per_page = 20
