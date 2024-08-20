from rest_framework.generics import CreateAPIView

from apps.common.models import Genre
from .serializer import GenreCreateSerializer


class GenreCreateView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreCreateSerializer
    