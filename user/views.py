from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def register(request):
		s = UserSerializer(data=request.data)
		if s.is_valid():
			s.save()
		return Response({'status':"account created"})

@csrf_exempt
@api_view(['POST'])
def login(request):
		s = UserSerializer(data=request.data)
		if s.is_valid():
			user = User.objects.get(username=s.data["username"], password=s.data["password"])
		return Response({'status':"success",'userId':user.id})
