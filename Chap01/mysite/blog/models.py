from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                    .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    # Status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Publised'

    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # default manager
    objects = models.Manager()
    # custom manager
    published = PublishedManager()

    # class to sorted Post
    # this class define metadata for the model
    class Meta:
        ordering = ['-publish']
        # index database improve performance for quries filtering
        # or ordering results by this field
        indexes = [
            models.Index(fields=['-publish'])
        ]

    # return str to human redeable
    def __str__(self):
        return self.title