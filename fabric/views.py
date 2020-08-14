from rest_framework import viewsets
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FabricTypeViewSet(viewsets.ModelViewSet):
    queryset = FabricType.objects.all().order_by('type')
    serializer_class = FabricTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class FabricContentViewSet(viewsets.ModelViewSet):
    queryset = FabricContent.objects.all().order_by('content')
    serializer_class = FabricContentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class RecommendedUseViewSet(viewsets.ModelViewSet):
    queryset = RecommendedUse.objects.all().order_by('uses')
    serializer_class = RecommendedUseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class DesignElementViewSet(viewsets.ModelViewSet):
    queryset = DesignElement.objects.all().order_by('design_elements')
    serializer_class = DesignElementSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class ColorFamilyViewSet(viewsets.ModelViewSet):
    queryset = ColorFamily.objects.all().order_by('color_family')
    serializer_class = ColorFamilySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class FabricBrandViewSet(viewsets.ModelViewSet):
    queryset = FabricBrand.objects.all().order_by('fabric_brand')
    serializer_class = FabricBrandSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class FabricCollectionViewSet(viewsets.ModelViewSet):
    queryset = FabricCollection.objects.all().order_by('collection')
    serializer_class = FabricCollectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.all().order_by('name')
    serializer_class = DesignerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class FabricViewSet(viewsets.ModelViewSet):
    queryset = Fabric.objects.all().order_by('name')
    serializer_class = FabricSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
