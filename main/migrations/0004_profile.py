# Generated by Django 4.2.3 on 2023-08-01 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_cinemahall_genre_movie_director_movie_poster_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Картинка должна быть Х на Х', null=True, upload_to='profile/', verbose_name='Фотография')),
                ('balance', models.PositiveIntegerField(default=0, verbose_name='Баланс')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[main.utils.validate_phone_number], verbose_name='Номер телефона')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('about', models.TextField(blank=True, max_length=200, null=True, verbose_name='Обо мне')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['-created_at'],
            },
        ),
    ]
