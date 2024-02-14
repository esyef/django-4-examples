from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    # Status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Publised'

    
    title = models.CharField(max_lengh=250)
    slug = models.SlugField(max_lenght=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    status = models.TextChoices(max_lenght= 2, choices=Status.choices, default=Status.DRAFT)


    # class to sorted Post
    # this class define metadata for the model
    class Meta:
        ordering = ['-publish']
        # index database improve performance for quries filtering
        # or ordering results by this field
        index = [
            models.Index(fields=['-publish'])
        ]

    # return str to human redeable
    def __str__(self):
        return self.title