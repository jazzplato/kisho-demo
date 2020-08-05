from django.contrib import admin
from .models import Movie, MovieRating


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass


class MovieRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)