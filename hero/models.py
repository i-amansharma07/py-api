from django.db import models

class Hero(models.Model):
    fname  =  models.CharField(max_length=50)
    lname = models.CharField(max_length=50) 	
