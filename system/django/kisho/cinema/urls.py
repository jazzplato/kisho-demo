from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'movies', views.MovieViewSet, basename="movies")
router.register(r'ratings', views.MovieRatingViewSet, basename="ratings")
router.register(r'health', views.HealthViewSet, basename="health")

urlpatterns = [
    path('', include(router.urls)),
    path('welcome', views.welcome, name='welcome'),
    path('rate', views.rate_movie, name='rate'),
]