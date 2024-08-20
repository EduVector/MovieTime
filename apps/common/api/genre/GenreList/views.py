from rest_framework.generics import ListAPIView

from apps.common.models import Genre
from .serializer import GenreListSerializer


class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    