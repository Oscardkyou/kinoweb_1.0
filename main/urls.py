# urls.py
from django.urls import path
from .views import index, a, index2, movie_details, cinema_seats
from django.contrib.auth import views as auth_views


urlpatterns = [
      path('', index, name='index2'),
      path('login/', auth_views.LoginView.as_view(), name='login'),
      path('a/', a, name='a'),
      path('index/', index2, name='index'),
      path('movie-details/<int:movie_id>/', movie_details, name='movie-details'),
      path('cinema_seats/<int:screening_id>/', cinema_seats, name='cinema_seats'),
]
