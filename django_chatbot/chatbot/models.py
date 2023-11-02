from django.db import models
from django.contrib.auth.models import User
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField()
#
# def __self__:
#     return f'{self.user.username}'
