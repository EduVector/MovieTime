from rest_framework.serializers import ModelSerializer

from apps.common.models import Genre


class GenreListSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'uuid',
            "name",
            "parent",
            "created_at",
        )
