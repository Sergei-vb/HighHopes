from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from models import Profile
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def profiles_list(request):
     profiles = Profile.objects.all()
     return render(request, 'profiles.html', {'profiles': profiles})


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/profiles_list/"

    template_name = "register.html"

    def form_valid(self, form):

        instance = form.save(commit=False)

        instance.os = self.request.user_agent.os.family + ' ' + self.request.user_agent.os.version_string
        instance.language = self.request.META.LANGUAGE

        instance.save()

        return super(RegisterFormView, self).form_valid(form)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')