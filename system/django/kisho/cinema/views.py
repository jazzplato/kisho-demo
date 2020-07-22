from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Movie, MovieRating
from .serializers import UserSerializer, MovieSerializer


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Kisho Cinema!")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-registered_at')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer