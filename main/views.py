# views.py
from django.shortcuts import render, redirect
from .models import Movie, Screening, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm


def cinema_seats(request):
    row = request.GET.get()

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


def LogoutUser(request):
    logout(request, "Вы успешно вышли из учетной записи!")
    return redirect('/')


def Login(request):
    logout(request)
    return redirect('/')


def SignInUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request,
                                username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли!')
                return redirect('/')
            else:
                messages.error(request, "Неверное имя пользоватля!")
        else:
            messages.error(request, "Введите имя пользоватлея!")
    return render(request, 'AuthenticateUser/singin.html')


def SignUpUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password == request.POST.get('password2'):
                messages.error(request, "Пароли не совпадют")
                return redirect('/singup')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, "Регистрация прошла успешна!")
                return redirect("/")
    else:
        form = UserForm()
    return render(request, 'AuthenticateUser/singup.html',
                  {"form": form})

