from django.db import models
from django.contrib.auth.models import User
from .utils import validate_phone_number

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # предположим, что здесь есть другие поля...

    def __str__(self):
        return self.user.username  # Предполагая, что в модели Profile есть поле user.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    duration = models.IntegerField(default=0, verbose_name="Длительность")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name="Описание")
    director = models.CharField(max_length=100, blank=True, null=True, verbose_name="Режиссёр")
    release_year = models.IntegerField(blank=True, null=True, verbose_name="Год выпуска")
    poster = models.ImageField(upload_to='posters/', blank=True, null=True, verbose_name="Постер")
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    quality = models.CharField(max_length=10, choices=[('HD', 'HD'), ('2K', '2K'), ('4K', '4K')], verbose_name="Качество", default='HD')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")

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
