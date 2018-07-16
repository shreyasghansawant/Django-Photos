from django.db import models
from django.contrib.auth.models import User
import datetime


# Photos
class Photo (models.Model):
    image = models.ImageField (upload_to='images/')
    title = models.CharField (max_length=25)
    description = models.TextField (default=None, max_length=500)
    num_like = models.IntegerField (default=0)
    author = models.ForeignKey (User, on_delete=models.CASCADE)
    date_time = models.DateTimeField (default=datetime.datetime.now())

    def __str__(self):
        return self.title

# Like
class Like (models.Model):
    image = models.ForeignKey (Photo, on_delete=models.CASCADE)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    like = models.BooleanField (default=False)

    def __str__(self):
        return self.image.title + ' - ' + self.user.username


# Comment
class Comment (models.Model):
    image = models.ForeignKey (Photo, on_delete=models.CASCADE)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    comment = models.CharField (max_length=100)

    def __str__(self):
        return self.image.title + ' - ' + self.user.username
