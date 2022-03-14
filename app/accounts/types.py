import strawberry
from django.contrib.auth import get_user_model
from strawberry.django import auto


@strawberry.django.type(get_user_model())
class User:
    username: auto
    email: auto


@strawberry.django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
