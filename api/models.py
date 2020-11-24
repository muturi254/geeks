from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name="Todo", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="Todo", on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)