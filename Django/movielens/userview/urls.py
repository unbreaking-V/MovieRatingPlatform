from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path('movies/', views.movies_view, name='movies'),
    path("movie/<int:movie_id>", views.view_movie, name="index"),
    path("register/", views.register_request, name="register"),
    path("login/", views.user_login, name="login"),
    path('logout/', views.logout_request, name='logout'),
    path('ratings/', views.ratings, name='ratings'),
]