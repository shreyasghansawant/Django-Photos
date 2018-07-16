from django.urls import path
from . import views

app_name = "photos"

urlpatterns = [

    # USER

    # User Accounts --> SignUp, LogIn, LogOut
    path ('accounts/signup/', views.SignUpView, name="signup"),
    path ('accounts/login/', views.LogInView, name="login"),
    path ('accounts/logout/', views.LogOutView, name="logout"),

    # PHOTOS

    # photo
    path ('', views.IndexView, name="index"),
    path ('<int:photo_id>/', views.DetailView, name="detail"),

    # Comment
    path ('comment/<int:photo_id>', views.CommentView, name="comment"),
    path ('comment/<int:photo_id>/view/', views.ViewComments, name="view-comments"),

    # Like
    path ('like/<int:photo_id>/', views.LikePhoto, name="like"),

    # Add Photo
    path ('add/photo/', views.AddPhotoView, name="add-photo"),

    # Update Photo
    path ('update/<int:photo_id>/', views.UpdatePhotoView, name="update"),

    # Delete Photo
    path ('delete/<int:photo_id>/', views.DeletePhotoView, name="delete"),

    # MORE

    # User Profile and Photos --> My Profile, Others Profile
    path ('myprofile/', views.MyProfileView, name="my-profile"),
    path ('profile/<int:photo_id>/', views.ProfileView, name="profile"),

    # Search
    path ('search/', views.Search, name="search"),

    # About
    path ('about/', views.About, name="about"),

]
