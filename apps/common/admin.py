from django.contrib import admin

from apps.common.models import Country, Category, Actor, Award, Genre

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Award)
admin.site.register(Genre)

