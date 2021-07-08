from django.db import models


# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=50)


class Flashcard(models.Model):
    collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=100)
