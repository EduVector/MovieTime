from django.contrib import admin

from apps.movie.models import Movie, MovieImage, Review, MovieFile, AdditionalInfo, Liked

admin.site.register(Movie)
admin.site.register(MovieImage)
admin.site.register(Review)
admin.site.register(MovieFile)
admin.site.register(AdditionalInfo)
admin.site.register(Liked)
