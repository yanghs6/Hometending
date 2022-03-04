from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name="account"
urlpatterns = [
    # path("login/", views.login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", views.signup, name="signup"),
]
