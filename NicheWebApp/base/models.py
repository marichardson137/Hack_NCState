from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=255, default=None)
    image = models.ImageField(upload_to='images/', default=None)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
