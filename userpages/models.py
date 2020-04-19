from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accountUser')
    profilePic = models.ImageField(upload_to='userpages', default='userpages/def_face.jpg')
    bio = models.TextField(blank=True)
    friends = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Kein Titel')
    dateLaunched = models.DateTimeField(auto_now_add=True)
    textContent = models.TextField(max_length=300)

    def __str__(self):
        return self.title
