from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserData, Post, Blog
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserDataForm, SignUpForm


def home(request):

    users = UserData.objects.all()
    blogs = Blog.objects.all()
    try:
        personalBlogs = Blog.objects.filter(user=UserData.objects.get(user=request.user))
        return render(request, 'userpages/home.html', {'users': users, 'blogs': blogs, 'personalBlogs': personalBlogs})
    except TypeError:

        return render(request, 'userpages/home.html', {'users':users, 'blogs':blogs})


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'userpages/home.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'userpages/home.html', {'error':'Benutzername oder Passwort ist falsch'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'userpages/signUpUser.html', {'form':SignUpForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                userdata = UserData(user=user)
                userdata.save()
                return redirect('mySite')
            except IntegrityError:
                return render(request, 'userpages/signUpUser.html', {'form':SignUpForm, 'error':'Ungültige Eingabe.'})
        else:
            return render(request, 'userpages/signUpUser.html', {'form': SignUpForm, 'error': 'Keine Übereinstimmung der Passwörter.'})

@login_required
def account(request, user_pk):
    try:
        useraccount = UserData.objects.get(pk=user_pk)
        user = UserData.objects.get(user=request.user)
        userFriends = user.friends.split(',')
        friendNumber = len(userFriends) - 1

        if str(user_pk) in userFriends:
            friend = True
        else:
            friend = False

        blogs = Blog.objects.filter(user=user)

        return render(request, 'userpages/account.html', {'useraccount':useraccount, 'friend':friend, 'friendNumber':friendNumber, 'blogs':blogs})
    except ObjectDoesNotExist:
        return redirect('home')


@login_required
def mySite(request):
    if request.method == 'GET':
        try:
            userData = UserData.objects.get(user=request.user)
            form = UserDataForm(instance=UserData.objects.get(user=request.user))
            return render(request, 'userpages/mySite.html', {'form':form})
        except ObjectDoesNotExist:
            form = UserDataForm()
            return render(request, 'userpages/mySite.html', {'form':form})
    else:
        try:
            form = UserDataForm(request.POST, instance=UserData.objects.get(user=request.user))
            form.save()
            return render(request, 'userpages/mySite.html', {'form':form, 'success':'Erfolgreich geändert.'})
        except ValueError:
            return render(request, 'userpages/mySite.html', {'form':form, 'error':'Bad data.'})


def follow(request):
    if request.method == 'GET':
        return redirect('home')
    else:
        userdata = UserData.objects.get(user=request.user)
        pk = request.POST['pk']
        friendsStr = userdata.friends
        print(friendsStr)
        if len(friendsStr) == 0:
            userdata.friends = pk + ','
            userdata.save()
        else:
            friends = friendsStr.split(',')
            if pk in friends:
                friends.remove(pk)
                userdata.friends = ','.join(friends)
                userdata.save()
            else:
                userdata.friends = friendsStr + pk + ','
                userdata.save()

        return redirect('account', user_pk=pk)


@login_required
def freunde(request):
    userData = UserData.objects.get(user=request.user)
    friendIds = userData.friends.split(',')
    friendIds.pop()
    friends = []
    for friend in friendIds:
        friends.append(UserData.objects.get(pk=friend))

    print(friends)

    return render(request, 'userpages/freunde.html', {'friends':friends})


@login_required
def newPost(request):
    if request.method == 'GET':

        return render(request, 'userpages/newPost.html')
    else:
        post = Post.objects.create(user=UserData.objects.get(user=request.user), textContent=request.POST['postText'])
        return redirect('home')

@login_required
def blogdetail(request, blog_pk):

    blog = Blog.objects.get(pk=blog_pk)
    posts = Post.objects.filter(blog=blog)

    return render(request, 'userpages/blog.html', {'blog':blog, 'posts':posts})


