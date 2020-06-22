from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class GroupModel(models.Model):
	member =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	group =  models.CharField(max_length=60)
	created_by = models.CharField(max_length = 60)


class TaskAssignModel(models.Model):
	assigned_to = models.ForeignKey(GroupModel,on_delete=models.CASCADE,null=True)
	task = models.CharField(max_length=60)
	assigned_by = models.CharField(max_length = 60)
	
		