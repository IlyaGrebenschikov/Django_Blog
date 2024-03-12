from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from main import views


urlpatterns = [
    path('', views.index, name='home'),
]