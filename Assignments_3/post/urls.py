from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("", views.post_list, name="list"),
    path("create/", views.post_create, name="create"),
    path("<int:pk>/delete/", views.post_delete, name="delete"),
    path("<int:pk>/", views.post_detail, name="detail"),
    path("<int:pk>/update/", views.post_update, name="update"),
]
