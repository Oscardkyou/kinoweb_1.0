from django.contrib.auth.models import User
from django.forms import (EmailInput, ModelForm, PasswordInput, TextInput)



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "First name",
            }),
            "last_name": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Last name",
            }),
            "username": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Username",
            }),
            "email": EmailInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "E-mail",
            }),
            "password": PasswordInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Password",
            }),
        }