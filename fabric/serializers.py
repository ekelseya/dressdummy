from rest_framework import serializers
from .models import *


class FabricTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricType
        fields = '__all__'


class RecommendedUsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedUses
        fields = '__all__'


class DesignElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignElements
        fields = '__all__'


class ColorFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorFamily
        fields = '__all__'


class FabricBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricBrand
        fields = '__all__'


class FabricCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricCollection
        fields = '__all__'


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = '__all__'


class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = '__all__'
