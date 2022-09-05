from rest_framework import serializers
from .models import Hero
from dataclasses import fields
class HeroSerializer(serializers.ModelSerializer):
	class Meta :
		model = Hero
		fields = ['id', 'fname', 'lname']
