import datetime
from rest_framework import serializers, fields
from django.contrib.auth.models import User
from .models import Movie, MovieRating
from .constants import RATING_MIN, RATING_MAX
from .utils import calc_overall_rating


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ["id", "user", "movie", "rating", "factor", "factored_rating"]
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    date_joined = fields.DateTimeField(
        input_formats=["%Y-%m-%d"],
        initial=datetime.datetime.today().date(),
        required=False)

    class Meta:
        model = User
        fields = ["username", "password", "date_joined", "movies"]
        depth = 1

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MovieSerializer(serializers.ModelSerializer):
    overall_rating = serializers.SerializerMethodField()
    rating_time = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            "id", "title", "year", "ratings", "overall_rating", "rating_time"
        ]
        depth = 1

    def get_overall_rating(self, obj):
        ratings = obj.ratings.all()
        overall_rating = calc_overall_rating(ratings)
        return overall_rating

    def get_rating_time(self, obj):
        return datetime.datetime.now()


class RateRequestSerializer(serializers.Serializer):
    movie_id = fields.IntegerField(min_value=0)
    rating = fields.IntegerField(min_value=RATING_MIN, max_value=RATING_MAX)