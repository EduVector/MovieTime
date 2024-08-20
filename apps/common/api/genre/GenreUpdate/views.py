from rest_framework.generics import UpdateAPIView

from apps.common.models import Genre
from .serializer import GenreUpdateSerializer


class GenreUpdateView(UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreUpdateSerializer
    lookup_field = 'name'

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    