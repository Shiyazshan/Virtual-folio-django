from django.contrib import admin
from works.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "title", "description"]
admin.site.register(Service)