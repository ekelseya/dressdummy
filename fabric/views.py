from .serializers import *
from rest_framework import viewsets


class FabricTypeViewSet(viewsets.ModelViewSet):
    queryset = FabricType.objects.all()
    serializer_class = FabricTypeSerializer


class RecommendedUsesViewSet(viewsets.ModelViewSet):
    queryset = RecommendedUses.objects.all()
    serializer_class = RecommendedUsesSerializer


class DesignElementsViewSet(viewsets.ModelViewSet):
    queryset = DesignElements.objects.all()
    serializer_class = DesignElementsSerializer


class ColorFamilyViewSet(viewsets.ModelViewSet):
    queryset = ColorFamily.objects.all()
    serializer_class = ColorFamilySerializer


class FabricBrandViewSet(viewsets.ModelViewSet):
    queryset = FabricBrand.objects.all()
    serializer_class = FabricBrandSerializer


class FabricCollectionViewSet(viewsets.ModelViewSet):
    queryset = FabricCollection.objects.all()
    serializer_class = FabricCollectionSerializer


class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.all()
    serializer_class = DesignerSerializer


class FabricViewSet(viewsets.ModelViewSet):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer
