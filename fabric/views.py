from .serializers import *
from rest_framework import viewsets


class FabricTypeViewSet(viewsets.ModelViewSet):
    queryset = FabricType.objects.all().order_by('type')
    serializer_class = FabricTypeSerializer


class FabricContentViewSet(viewsets.ModelViewSet):
    queryset = FabricContent.objects.all().order_by('content')
    serializer_class = FabricContentSerializer


class RecommendedUseViewSet(viewsets.ModelViewSet):
    queryset = RecommendedUse.objects.all().order_by('uses')
    serializer_class = RecommendedUseSerializer


class DesignElementViewSet(viewsets.ModelViewSet):
    queryset = DesignElement.objects.all().order_by('design_elements')
    serializer_class = DesignElementSerializer


class ColorFamilyViewSet(viewsets.ModelViewSet):
    queryset = ColorFamily.objects.all().order_by('color_family')
    serializer_class = ColorFamilySerializer


class FabricBrandViewSet(viewsets.ModelViewSet):
    queryset = FabricBrand.objects.all().order_by('fabric_brand')
    serializer_class = FabricBrandSerializer


class FabricCollectionViewSet(viewsets.ModelViewSet):
    queryset = FabricCollection.objects.all().order_by('collection')
    serializer_class = FabricCollectionSerializer


class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.all().order_by('name')
    serializer_class = DesignerSerializer


class FabricViewSet(viewsets.ModelViewSet):
    queryset = Fabric.objects.all().order_by('name')
    serializer_class = FabricSerializer
