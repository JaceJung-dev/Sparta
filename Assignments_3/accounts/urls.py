from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("delete/", views.delete, name="delete"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
    path("profile/", views.user_profile, name="profile"),
]
