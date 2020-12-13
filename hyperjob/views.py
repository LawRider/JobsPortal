from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class MenuView(TemplateView):
    template_name = 'menu.html'
    entries = {"login": "Login",
               "signup": "Sign Up",
               "vacancies": "Vacancies",
               "resumes": "Resumes",
               "home": "Home"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = self.entries
        return context


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
