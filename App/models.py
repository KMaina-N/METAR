from django.db import models

# Create your models here.
class News(models.Model):
    posts = models.CharField(blank=False, max_length=10000)
    