from django.contrib import admin
from .models import User, Movie, MovieRating


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class MovieRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)