from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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


@method_decorator(login_required, name='dispatch')
class UserDetailView(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = 'accounts/details_view.html'
    context_object_name = 'user'

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        filtered_queryset = queryset.filter(pk=current_user.pk)
        return filtered_queryset


class MyLoginView(LoginView):
    model = MyUser
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home') 

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
    
class MyLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'home'
    http_method_names = ['get', 'post']