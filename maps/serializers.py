from rest_framework import serializers
from .models import Map, MapContent

class MapSerializer(serializers.ModelSerializer):
	class Meta:
		model = Map
		field = ('id', 'author', 'title', 'question', 'description', 'created_date', 'published_date')

class MapContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapContent
        field = ('id', 'map', 'content', 'created_date')