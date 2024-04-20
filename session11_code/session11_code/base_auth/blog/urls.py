from .views import home, new, detail, edit, delete, delete_comment
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("new/", new, name="new"),
    path("detail/<int:post_pk>", detail, name="detail"),
    path("edit/<int:post_pk>", edit, name="edit"),
    path("delete/<int:post_pk>", delete, name="delete"),
    path(
        "delete-comment/<int:comment_pk>",
        delete_comment,
        name="delete_comment",
    ),
    ]
