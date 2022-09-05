from curses.ascii import HT
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Hero
from .serializers import HeroSerializer


def Hero_list(request):
	hero = Hero.objects.all()
	serial = HeroSerializer(hero,many=True)
	return JsonResponse(serial.data, safe = False)

def root(request):
	return HttpResponse("This is root folder!!")