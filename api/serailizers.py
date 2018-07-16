from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from photos.models import Photo, Like, Comment


# USERS

class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# PHOTOS

# Photo
class PhotoSerializer (ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


# Like
class LikeSerializer (ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


# Comment
class CommentSerializer (ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
