from django.contrib import admin

from . import models

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Recording)
class RecordingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}