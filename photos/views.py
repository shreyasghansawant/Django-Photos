from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.conf import settings
from .models import Photo
from .forms import AddPhotoForm, AddCommentForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm


# USERS

# SignUp
def SignUpView(request):
    if request.method == "POST":
        form = SignUpForm (request.POST)

        if form.is_valid ():
            user = form.save ()
            login (request, user)

            # Send Email To User
            subject = 'Thanks For SigningUp'
            message = 'Welcome to Photos'
            admin = settings.EMAIL_HOST_USER
            user = user.email
            send_mail (subject, message, admin, [user], fail_silently=True)

            return redirect ('photos:index')

    else:
        form = SignUpForm ()

    return render (request, 'photos/signup.html', {'form': form})


# LogIn
def LogInView(request):
    if request.user:

        if request.method == "POST":
            form = AuthenticationForm (data=request.POST)

            if form.is_valid ():
                user = form.get_user ()
                login (request, user)
                return redirect ('photos:index')

        else:
            form = AuthenticationForm ()

        return render (request, 'photos/login.html', {'form': form})

    else:
        return redirect ("photos:login")


# LogOut
@login_required (login_url="photos:login")
def LogOutView(request):
    if request.method == "POST":
        logout (request)
        return redirect ('photos:index')


# PHOTOS

# Photo
def IndexView(request):
    all_photos = Photo.objects.all ().order_by ('-date_time')
    form = AddCommentForm()

    return render (request, 'photos/index.html', {
        'all_photos': all_photos,
        'form': form,
    })

def DetailView(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    form = AddCommentForm()

    return render(request, 'photos/detail.html', {
    'photo': photo,
    'form': form,
    })


# Like
@login_required (login_url="photos:login")
def LikePhoto(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get (pk=photo_id)
        try:
            check_like = photo.like_set.get (user=request.user)
            if check_like:
                return render (request, 'photos/try.html', {'photo': photo})
        except Exception:
            photo.num_like += 1
            user = request.user
            like = photo.like_set.create (image=photo, user=user, like=True)
            like.save ()
            photo.save ()

            return redirect ("photos:detail", photo_id)


# Comment --> Add, View
@login_required (login_url="photos:login")
def CommentView(request, photo_id):
    photo = Photo.objects.get (pk=photo_id)

    if request.method == "POST":
        form = AddCommentForm (request.POST)

        if form.is_valid ():
            instance = form.save (commit=False)
            instance.user = request.user
            instance.image = photo
            instance.save ()
            return redirect ('photos:view-comments', photo.id)


def ViewComments(request, photo_id):
    photo = Photo.objects.get (pk=photo_id)
    comments = photo.comment_set.all ()
    num_c = photo.comment_set.all ().count ()
    form = AddCommentForm()

    return render (request, 'photos/comment.html', {
        'photo': photo,
        'comments': comments,
        'num_c': num_c,
        'form': form,
    })


# Add Photo
@login_required ()
def AddPhotoView(request):
    if request.method == "POST":
        form = AddPhotoForm (request.POST, request.FILES)

        if form.is_valid ():
            instance = form.save (commit=False)
            instance.author = request.user
            instance.save ()
            return redirect ('photos:index')

    else:
        form = AddPhotoForm ()

    return render (request, 'photos/add-photo.html', {'form': form})


# Update Photo
@login_required ()
def UpdatePhotoView(request, photo_id):
    photo = Photo.objects.get (pk=photo_id)

    if request.user == photo.author:
        form = AddPhotoForm (request.POST or None, request.FILES or None, instance=photo)

        if request.method == "POST":
            if form.is_valid ():
                form.save ()
                return redirect ('photos:my-profile')

        return render (request, 'photos/add-photo.html', {'form': form})

    return redirect ('photos:index')


# Delete Photo
@login_required ()
def DeletePhotoView(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get (pk=photo_id)

        if request.user == photo.author:
            photo.delete ()
            return redirect ('photos:my-profile')


# MORE

# User Profile and Photos --> My Profile, Others Profile
@login_required (login_url="photos:login")
def MyProfileView(request):
    user = request.user
    user_email = user.email
    photos = Photo.objects.filter (author=user).order_by ('-date_time')
    return render (request, 'photos/my-profile.html', {
        'photos': photos,
        'user': user,
        'user_email': user_email,
    })


def ProfileView(request, photo_id):
    photo = Photo.objects.get (pk=photo_id)
    user = photo.author
    user_email = user.email
    form = AddCommentForm()

    if user == request.user:
        return redirect ("photos:my-profile")

    else:
        photos = Photo.objects.filter (author=user).order_by ('-date_time')

    return render (request, 'photos/profile.html', {
        'photos': photos,
        'user': user,
        'user_email': user_email,
        'form': form,
    })


# Search
def Search(request):
    if request.method == "GET":
        text = request.GET.get ('search_text', None)
        photos = Photo.objects.filter (title__contains=text).order_by ('-date_time')
        form = AddCommentForm()
        return render (request, 'photos/search.html', {
            'photos': photos,
            'text': text,
            'form': form,
        })


# About
def About(request):
    return render (request, 'photos/about.html', {})
