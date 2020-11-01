import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    # the url of author picture in the static folder
    image_url = models.CharField(max_length=250)
    bio = models.CharField(max_length=250)

     # return the name of an author record when queried
    def __str__(self):
        return self.name

class Catogory (models.Model):
    catogoryName = models.CharField(max_length = 50, null=True)

    # return the name of a category record when queried
    def __str__(self):
        return self.catogoryName


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    # the url of post picture in the static folder
    image_url = models.CharField(max_length=250)
    create_date = models.DateTimeField('date created')
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    catogory = models.ForeignKey(Catogory, on_delete=models.CASCADE, null=True)

    # return the title of a post record when queried
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)


