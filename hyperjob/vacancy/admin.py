from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
