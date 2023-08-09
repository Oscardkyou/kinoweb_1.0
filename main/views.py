# views.py
from django.shortcuts import render, redirect
from .models import Movie, Screening, Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    screenings = Screening.objects.all()
    return render(request, 'index2.html')


def a(request):
    return render(request, 'a.html')


def index2(request):
    movies = Movie.objects.all()
    screenings = Screening.objects.all()
    return render(request, 'index.html', {'movies': movies,'screenings': screenings,})


def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie-details.html', {'movie': movie})





