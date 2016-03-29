from rest_framework import serializers
from .models import Mapper


class MapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapper
        fields = ('user', 'birthday', 'name')