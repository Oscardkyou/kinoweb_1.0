from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Movie, Genre, CinemaHall, Screening, Booking, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'birth_date', 'phone', 'get_image')
    list_filter = ('birth_date',)
    search_fields = ('user__username', 'user__email')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px" />')
        return 'Not image'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'description', 'director', 'release_year', 'rating']
    list_filter = ['genre']

@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ['name', 'seat_count']

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ['movie', 'start_time', 'end_time', 'cinema_hall']
    list_filter = ['movie', 'cinema_hall']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['screening', 'user', 'seat_number']
    list_filter = ['screening', 'user']
