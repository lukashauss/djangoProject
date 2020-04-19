from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChessGame(models.Model):
    board = models.CharField(max_length=64, default='tsldklstbbbbbbbb                                BBBBBBBBTSLDKLST')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    moveCounter = models.IntegerField(auto_created=True, default=0)
