from django.db import models
from apps.utils.models.base_model import AbstractBaseModel


class Menu(AbstractBaseModel):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    checked = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    dimensions = models.TextField(blank=True)
    per_man_link = models.BooleanField(default=False)


    def __str__(self):
        return self.name
