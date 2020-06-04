from .serializers import *
from rest_framework import viewsets


class PatternCompanyViewSet(viewsets.ModelViewSet):
    queryset = PatternCompany.objects.all()
    serializer_class = PatternCompanySerializer


class PatternCollectionViewSet(viewsets.ModelViewSet):
    queryset = PatternCollection.objects.all()
    serializer_class = PatternCollectionSerializer


class PatternDesignerViewSet(viewsets.ModelViewSet):
    queryset = PatternDesigner.objects.all()
    serializer_class = PatternDesignerSerializer


class PatternTypeViewSet(viewsets.ModelViewSet):
    queryset = PatternType.objects.all()
    serializer_class = PatternTypeSerializer


class PatternViewSet(viewsets.ModelViewSet):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternSizeViewSet(viewsets.ModelViewSet):
    queryset = PatternSize.objects.all()
    serializer_class = PatternSizeSerializer


class PatternFinishedMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PatternFinishedMeasurement.objects.all()
    serializer_class = PatternFinishedMeasurementSerializer
