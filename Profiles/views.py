# -*- coding: utf-8 -*- #
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from models import Profile
from django.contrib.auth.decorators import login_required

# from .forms import

def index(request):
    return render(request, 'index.html')

# def login(request):
#     return render(request, 'login.html')

def profiles_list(request):
     profiles = Profile.objects.all()
     return render(request, 'profiles.html', {'profiles': profiles})

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/profiles_list/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):

        instance = form.save(commit=False)

        #заполняем свойства объекта, которых у него нет! это норм??
        instance.os = self.request.user_agent.os.family + ' ' + self.request.user_agent.os.version_string
        instance.language = self.request.META.LANGUAGE; #?????

        instance.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')