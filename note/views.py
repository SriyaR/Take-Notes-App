from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def addNote(request):
		user = request.GET["user"]
		data = request.data
		_mutable = data._mutable
		data._mutable = True
		data = request.data
		data["id"] = user
		data._mutable = _mutable
		s = NoteSerializer(data=data)
		if s.is_valid():
			s.save()
		return Response({'status':"success"})

@csrf_exempt
@api_view(['GET'])
def index(request):
		user = request.GET["user"]
		data = {}
		data["id"] = user
		s = NoteSerializer(data=data)
		if s.is_valid():
			note = Note.objects.get(userId = user)
			return Response({'status':"success",'note':note})
		return Response({"status":"error"})
