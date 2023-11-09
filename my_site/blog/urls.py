from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.index, name="index"), 
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail")
]