from django.db import models
from user.models import User
# Create your models here.
class Note(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	note = models.CharField(max_length=500)