from rest_framework import serializers
from .models import *


class PatternCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternCompany
        fields = '__all__'


class PatternCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternCollection
        fields = '__all__'


class PatternDesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternDesigner
        fields = '__all__'


class PatternTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternType
        fields = '__all__'


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = '__all__'


class PatternViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternView
        fields = '__all__'
