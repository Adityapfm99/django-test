from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    mpaaRating = models.CharField(max_length=100)
    userRating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name