from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Room(models.Model):
    room_name=models.CharField(max_length=128)
    def __str__(self):
        return self.room_name

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    author1=models.ForeignKey(Room,related_name="message1",on_delete=models.CASCADE,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
class details(models.Model):
    author=models.ForeignKey(User,related_name='author_friends',on_delete=models.CASCADE)
