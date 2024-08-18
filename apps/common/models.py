from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, db_index=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
