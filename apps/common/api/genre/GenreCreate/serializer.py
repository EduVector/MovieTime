from rest_framework.serializers import ModelSerializer

from apps.common.models import Genre


class GenreCreateSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'uuid',
            "name",
            "parent",
            "created_at",
        )
        
        extra_kwargs = {
            "uuid": {"read_only": True},
            "created_at": {"read_only": True},
        }
        