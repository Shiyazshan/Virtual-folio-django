from django.contrib import admin
from works.models import Service, Project, Category


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "title", "description"]
admin.site.register(Service)

admin.site.register(Project)
admin.site.register(Category)