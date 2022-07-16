from django.urls import path
from . import views

urlpatterns = [
    path("post", views.getPosts),
    path("post/create", views.createPost),
    path("post/<str:pk>/update/", views.updatePost),
    path("post/<str:pk>/delete/", views.deletePost),
    path("post/<str:pk>", views.getPost)
]
