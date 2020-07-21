from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	username = serializers.CharField(
            required=True,
            label="username"
    )
	password = serializers.CharField(
			required=True,
			label="password",
			style={'input_type':'password'}
	)
	class Meta:
		model = User
		fields = ['username', 'password']  
	def create(self, data):
		return User.objects.create(**data)
