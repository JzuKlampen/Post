from datetime import datetime, date

from django.contrib.auth.models import User
from django.db import models


# Create your models here

class Post(models.Model):
    POST_TYPES = [
        ('BR', 'Breaking News'),
        ('Response', 'Response'),
        ('JK', 'Just kidding'),
        ('MT', 'My Thoughts'),
        ('NH', 'Need Help')
    ]

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=750)
    author = models.CharField(max_length=50)

    mood = models.CharField(max_length=50)
    date_published = models.DateTimeField(default=date.today)
    type = models.CharField(max_length=2,
                            choices=POST_TYPES,
                            )

    class Meta:
        ordering = ['author', 'title', '-type', 'text']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_full_title(self):
        return_string = self.title
        return return_string

    def __str__(self):
        return self.title + ' (' + self.author + '): ' + self.text

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.author + ' / ' + self.type

