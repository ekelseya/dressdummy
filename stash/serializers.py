from rest_framework import serializers
from .models import PatternStash, FabricStash


class PatternStashSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatternStash
        fields = '__all__'


class FabricStashSerializer(serializers.ModelSerializer):

    class Meta:
        model = FabricStash
        fields = '__all__'
