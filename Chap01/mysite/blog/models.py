from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_lengh=250)
    slug = models.SlugField(max_lenght=250)
    body = models.TextField()

    def __str__(self):
        return self.title