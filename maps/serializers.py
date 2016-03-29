from rest_framework import serializers
from .models import Map

class MapSerializer(serializers.ModelSerializer):
	class Meta:
		model = Map
		field = ('id', 'author', 'title', 'question', 'description', 'created_date', 'published_date')