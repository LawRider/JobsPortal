from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import Vacancy


class VacanciesListView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', {'vacancies': vacancies})


class AddVacancyView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            desc = request.POST.get('description')
            Vacancy.objects.create(author=request.user, description=desc)
            return redirect('/vacancies/')
        else:
            raise PermissionDenied
