from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
	userId = serializers.IntegerField(
			required=True,
			label="userId"
	)
	note = serializers.CharField(
            required=True,
            label="note"
    )
	class Meta:
		model = Note
		fields = ['userId','note']  
	def create(self, data):
		return Note.objects.create(**data)
