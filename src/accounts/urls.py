from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user-details')
]
