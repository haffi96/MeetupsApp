from django.db import models
from django.db.models.fields import SlugField

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
