from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Series(models.model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name