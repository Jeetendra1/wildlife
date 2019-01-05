from django.db import models


# Create your models here.

class Registration(models.Model):
	name = models.CharField(max_length = 25)
	email = models.CharField(max_length=30)
	contact = models.IntegerField(11)
	gender = models.CharField(max_length=5)
	
	def __str__(self):
		return self.name


class Address(models.Model):

	user_address = models.CharField(max_length = 50)
	country = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	registration = models.ForeignKey(Registration,on_delete = models.CASCADE)
	delete = models.IntegerField(5)

	def __str__(self):
		return self.user_address


 
	 
    