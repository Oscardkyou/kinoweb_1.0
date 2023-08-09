from django.db import models
from django.contrib.auth.models import User
from .utils import validate_phone_number

class Profile(models.Model):
    image = models.ImageField(upload_to="profile/",
        verbose_name="Фотография", help_text="Картинка должна быть Х на Х",
        blank=True, null=True)

    balance = models.PositiveIntegerField(default=0, verbose_name="Баланс")

    phone = models.CharField(max_length=20, unique=True,
        verbose_name="Номер телефона", blank=True, null=True,
        validators=[validate_phone_number])

    birth_date = models.DateField(verbose_name="Дата рождения",
        blank=True, null=True)

    about = models.TextField(max_length=200,
        verbose_name="Обо мне", blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE,
        verbose_name="Пользователь")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.first_name.title()} {self.user.last_name.title()[0]}."

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["-created_at"]


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    description = models.TextField(max_length=200, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class CinemaHall(models.Model):
    name = models.CharField(max_length=100, null=True)
    seat_count = models.IntegerField()

    def __str__(self):
        return self.name

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings', null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name='screenings', null=True)

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}"

class Booking(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE, related_name='bookings', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', null=True)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
