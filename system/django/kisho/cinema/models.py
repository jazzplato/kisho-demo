import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from .constants import MOVIE_YEAR_MIN, MOVIE_YEAR_MAX, RATING_MIN, RATING_MAX


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, blank=False)
    year = models.IntegerField(_("year"),
                               validators=[
                                   MinValueValidator(MOVIE_YEAR_MIN),
                                   MaxValueValidator(MOVIE_YEAR_MAX)
                               ])

    class Meta:
        unique_together = ["title", "year"]

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


class MovieRating(models.Model):
    user = models.ForeignKey(User,
                             related_name="movies",
                             on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,
                              related_name="ratings",
                              on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX)
        ],
    )
    factor = models.FloatField(default=0)
    factored_rating = models.FloatField(default=0)

    class Meta:
        unique_together = ['user', 'movie']