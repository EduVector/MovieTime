from rest_framework.generics import DestroyAPIView

from apps.common.models import Genre
from .serializer import GenreDestroySerializer


class GenreDestroyView(DestroyAPIView):
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreDestroySerializer
    lookup_field = "name"

    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
