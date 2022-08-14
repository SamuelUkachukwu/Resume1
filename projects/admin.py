from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'languages')
    list_filter = ('title',)
    search_fields = ['title', 'languages', 'github_link']


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'twitter',
        'github',
        'linkedin',
        'email',
        'phone_number'
        )