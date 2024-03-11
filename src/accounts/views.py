from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import MyCreationForm
from .models import MyUser


# Create your views here.
class UserRegistrationView(CreateView):
    template_name = 'accounts/form.html'
    form_class = MyCreationForm

    def form_valid(self, form):
        form.save()
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class UserDetailView(DetailView):
    model = MyUser
    template_name = 'accounts/details_view.html'
    context_object_name = 'user'
