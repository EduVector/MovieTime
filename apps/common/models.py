from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        db_index=True,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=225)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self):
        return self.name


class Award(BaseModel):
    name = models.CharField(max_length=225)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    STATUS = (
        (0, "Movie"),
        (1, "News"),
    )
    name = models.CharField(max_length=225)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name


class Actor(BaseModel):
    TYPES = (
        (0, "Actor"),
        (1, "Regisseur"),
    )
    name = models.CharField(max_length=225)
    type = models.IntegerField(choices=TYPES, default=0)

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
