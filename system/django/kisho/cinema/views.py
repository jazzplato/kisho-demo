from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Movie, MovieRating
from .serializers import UserSerializer, MovieSerializer, MovieRatingSerializer, RateRequestSerializer
from .utils import calc_rating_factor


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Kisho Cinema!")


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rate_movie(request, format=None):
    RateRequestSerializer(data=request.data).is_valid(raise_exception=True)
    user = request.user
    data = request.data
    rating = data.get("rating")
    movie_id = data.get("movie_id")
    factor = calc_rating_factor(user.date_joined)
    factored_rating = rating * factor
    try:
        movie = Movie.objects.get(pk=movie_id)
        movie_rating = MovieRating.objects.get(movie=movie, user=user)
        movie_rating.rating = rating
        movie_rating.factor = factor
        movie_rating.factored_rating = factored_rating
    except Movie.DoesNotExist:
        error = {'error_msg': 'No movie found with id: {}'.format(movie_id)}
        return Response(error)
    except MovieRating.DoesNotExist:
        movie_rating = MovieRating.objects.create(
            user=user,
            movie=movie,
            rating=rating,
            factor=factor,
            factored_rating=factored_rating)
    movie_rating.save()
    serializer = MovieRatingSerializer(movie_rating)
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer


class MovieRatingViewSet(viewsets.ModelViewSet):
    queryset = MovieRating.objects.all().order_by('-id')
    serializer_class = MovieRatingSerializer
