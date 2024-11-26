from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
