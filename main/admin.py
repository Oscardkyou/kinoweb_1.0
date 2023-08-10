from django.contrib import admin
from django.utils.html import format_html
from .models import Movie, CinemaHall, Screening, Booking, Profile #Genre

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'get_image')
    search_fields = ('user__username', 'user__email')

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'User'

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150px" />', obj.image.url)
        return 'Not image'
    get_image.short_description = 'Image'

# @admin.register(Genre)
# class GenreAdmin(admin.ModelAdmin):
#     list_display = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'description', 'director', 'release_year', 'rating', 'get_poster']
    #list_filter = ['genre']
    search_fields = ['title', 'director']

    def get_poster(self, obj):
        if obj.poster:
            return format_html('<img src="{}" width="50px" />', obj.poster.url)
        return 'No poster'
    get_poster.short_description = 'Poster'

@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ['name', 'seat_count']

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ['movie', 'start_time', 'end_time', 'cinema_hall']
    list_filter = ['movie', 'cinema_hall']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['screening', 'user_username', 'seat_number']
    list_filter = ['screening', 'user']

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'User'
