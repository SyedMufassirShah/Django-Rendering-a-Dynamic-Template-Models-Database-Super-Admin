from django.contrib import admin
from . import models

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(models.schools, SchoolAdmin)