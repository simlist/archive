from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'series'

class Recording(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    date = models.DateField()
    audio = models.FileField(upload_to='recordings/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date',]