from django.contrib import admin
from .models import Resume


class ResumeAdmin(admin.ModelAdmin):
    fields = ('author', 'description')
    readonly_fields = ['author']


admin.site.register(Resume, ResumeAdmin)
