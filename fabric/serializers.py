from rest_framework import serializers
from .models import *


class FabricTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricType
        fields = '__all__'


class FabricContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricContent
        fields = '__all__'


class RecommendedUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedUse
        fields = '__all__'


class DesignElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignElement
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
