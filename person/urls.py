from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', login_user, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('loginn/', LoginView.as_view(), name="loginn")

]
