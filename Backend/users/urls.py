from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path
from . import views 

urlpatterns = [
    path("login/",ObtainAuthToken.as_view(), name="login"),
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("me/", views.UserMeView.as_view(), name="me"),
]