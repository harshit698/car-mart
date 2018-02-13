from django.db import models
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class car(models.Model):
	owner=models.ManyToManyField(User)
	name=models.CharField(max_length=150)
	model_year=models.CharField(max_length=150)
	price=models.CharField(max_length=150)
	color=models.CharField(max_length=150)
	horsepower=models.CharField(max_length=16)
	brand=models.CharField(max_length=150)
	stock=models.IntegerField(default=0)
	def __str__(self):
		return self.brand+" "+self.name

class extended(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="ext")
	value=models.CharField(default='0',max_length=150) 
	def __str__(self):
		return self.user.username
