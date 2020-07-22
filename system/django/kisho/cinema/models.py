import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    year = models.IntegerField(
        _("year"),
        validators=[MinValueValidator(1905),
                    MaxValueValidator(2025)],
        null=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    register_date = models.DateField(_("date"), default=datetime.date.today)

    def __str__(self):
        return self.username


class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
    )
    factor = models.FloatField(default=0)
    factored_rating = models.FloatField(default=0)