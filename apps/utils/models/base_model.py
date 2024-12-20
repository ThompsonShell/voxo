import uuid

from django.db import models
from django.conf import settings

class AbstractBaseModel(models.Model):
    """"
    Abstract base model with common fields for all models.

    Attributes:
         created_at (DateTimeField): Timestamp when the object is created.
         updated_at (DateTimeField): Timestamp when the object is last updated.
    """

    id = models.UUIDField(primary_key=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )

    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.id = str(uuid.uuid4())
        super().save(*args, **kwargs)