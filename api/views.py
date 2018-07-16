from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from photos.models import Photo, Like, Comment
from django.contrib.auth.models import User
from .serailizers import UserSerializer, PhotoSerializer, LikeSerializer, CommentSerializer


# USER

class UserAPI (generics.ListCreateAPIView):
    queryset = User.objects.all ()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all ()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


# PHOTOS

# Photo
class PhotoAPI (generics.ListCreateAPIView):
    queryset = Photo.objects.all ()
    serializer_class = PhotoSerializer
    permission_classes = (IsAdminUser,)


class PhotoAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all ()
    serializer_class = PhotoSerializer
    permission_classes = (IsAdminUser,)


# Like
class LikeAPI (generics.ListCreateAPIView):
    queryset = Like.objects.all ()
    serializer_class = LikeSerializer
    permission_classes = (IsAdminUser,)


class LikeAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all ()
    serializer_class = LikeSerializer
    permission_classes = (IsAdminUser,)


# Comment
class CommentAPI (generics.ListCreateAPIView):
    queryset = Comment.objects.all ()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminUser,)


class CommentAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all ()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminUser,)
