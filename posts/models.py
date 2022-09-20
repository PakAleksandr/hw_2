from django.db import models

# Create your models here.

POST_TYPE_CHOICES = (
    (1, 'Animals'),
    (2, 'Cars'),
    (3, 'Recipes'),
    (4, 'Nature'),
    (5, 'Other')
)
class Comment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    stars = models.IntegerField(null=True)
    type = models.IntegerField(choices=POST_TYPE_CHOICES, null=True)
