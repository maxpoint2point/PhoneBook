from django.contrib import admin
from .models import Phones, Logging


class LoggingInLine(admin.StackedInline):
    model = Logging
    extra = 0
    readonly_fields = ("user", "log", "date",)


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "manager",)
    list_display_links = ("id", "name", "phone",)
    list_filter = ("manager",)
    search_fields = ("name", "phone",)
    inlines = [LoggingInLine]
    save_on_top = True
    save_as = True
    fieldsets = (
        ("Данные контакта", {
            "fields": (("name", "phone", "manager"),)
        }),
    )


@admin.register(Logging)
class LoggingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "log",)
    list_display_links = ("id", "user", "date", "log",)
    list_filter = ("user", "date",)
    readonly_fields = ("id", "user", "date", "log",)

