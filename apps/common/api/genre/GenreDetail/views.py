from rest_framework.generics import RetrieveAPIView

from apps.common.models import Genre
from .serializer import GenreRetrieveSerializer


class GenreRetrieveView(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreRetrieveSerializer
    lookup_field = "name"

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    