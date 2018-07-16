from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [

    # USER
    path ('user/', views.UserAPI.as_view(), name="api-user"),
    path ('user/<int:pk>/', views.UserAPIDetail.as_view(), name="api-user-detail"),

    # PHOTOS

    # Photo
    path ('photo/', views.PhotoAPI.as_view(), name="api-photo"),
    path ('photo/<int:pk>', views.PhotoAPIDetail.as_view(), name="api-photo-detail"),

    # Like
    path ('photo/like/', views.LikeAPI.as_view(), name="api-like"),
    path ('photo/like/<int:pk>/', views.LikeAPIDetail.as_view(), name="api-like-detail"),

    # Comment
    path ('photo/comment/', views.CommentAPI.as_view(), name="api-comment"),
    path ('photo/comment/<int:pk>/', views.CommentAPIDetail.as_view(), name="api-comment-detail"),

]

urlpatterns = format_suffix_patterns (urlpatterns)
