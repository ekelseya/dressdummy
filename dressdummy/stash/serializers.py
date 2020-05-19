from rest_framework import serializers
from .models import PatternStash, FabricStash


class PatternStashSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatternStash
        fields = ['id', 'user', 'pattern', 'notes']


class FabricStashSerializer(serializers.ModelSerializer):

    class Meta:
        model = FabricStash
        fields = ('id', 'user', 'fabric', 'notes')
