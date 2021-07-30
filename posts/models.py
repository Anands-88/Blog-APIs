from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50) # for limited character and can also mention max length
    body = models.TextField() # for unlimited.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
                # "Here changes Display name of an  object in Django admin interaface "
                # original = self.title
                # can write self.author body or anything int and  str.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body