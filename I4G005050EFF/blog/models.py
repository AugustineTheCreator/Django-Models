from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-Created_Date']

    def __str__(self):
        return self.title

