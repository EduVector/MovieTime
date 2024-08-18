from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.common.models import BaseModel


class Movie(BaseModel):
    LANGUAGE = (
        (0, "Uzbek"),
        (1, "Russian"),
        (2, "English"),
    )
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, max_length=225, db_index=True)
    description = RichTextField(null=True, blank=True)
    genres = models.ManyToManyField('common.Genre', blank=True)
    awards = models.ManyToManyField('common.Award', blank=True)
    actors = models.ManyToManyField('common.Actor', blank=True, limit_choices_to={"type": 0}, related_name='actors')
    regisseurs = models.ManyToManyField('common.Actor', blank=True, limit_choices_to={"type": 1}, related_name='regisseurs')
    category = models.ForeignKey(
        'common.Category',
        on_delete=models.SET_NULL,
        related_name='movies',
        related_query_name='movie',
        null=True, blank=True,
        limit_choices_to={"status": 0}
    )
    country = models.ForeignKey(
        'common.Country',
        on_delete=models.SET_NULL,
        related_name='movies',
        related_query_name='movie',
        null=True, blank=True
    )
    language = models.IntegerField(choices=LANGUAGE, default=0)
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=225, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class MovieImage(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cadres/', null=True, blank=True)

    def __str__(self):
        return self.movie.name


class MovieFile(BaseModel):
    PROGRESSIVES = (
        (0, "240p"),
        (1, "360p"),
        (2, "480p"),
        (3, "720p"),
        (4, "1080p"),
    )
    progressive = models.IntegerField(choices=PROGRESSIVES, default=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return f"{self.movie.name}, {self.progressive}"


class AdditionalInfo(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='additional_info')
    key = models.CharField(max_length=225)
    value = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie}, {self.key}: {self.value}"


class Review(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, related_name='movie_reviews')
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie}, {self.user}, {self.rate}"


class Liked(BaseModel):
    LIKES = (
        (0, "Like"),
        (1, "Dislike"),
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, related_name='liked_movies')
    like = models.IntegerField(choices=LIKES, default=0)

    def __str__(self):
        return f"{self.movie}, {self.user}"
