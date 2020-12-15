from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Movie, MovieRating
from .serializers import UserSerializer, MovieSerializer, MovieRatingSerializer, RateRequestSerializer
from .utils import calc_rating_factor
from .decorators import check_cache

SERVICE_START_TIME = datetime.now()


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Kisho Cinema!")


class HealthViewSet(viewsets.ViewSet):
    def list(self, request):
        uptime = (datetime.now() - SERVICE_START_TIME).total_seconds()
        data = {'uptime': '{} seconds'.format(uptime)}
        return Response(data, status=status.HTTP_200_OK)


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


class MovieRatingViewSet(viewsets.ModelViewSet):
    queryset = MovieRating.objects.all().order_by('-id')
    serializer_class = MovieRatingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer

    @check_cache
    def list(self, request):
        queryset = Movie.objects.all().order_by('-id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @check_cache
    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all().order_by('-id')
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
