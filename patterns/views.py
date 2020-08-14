from .serializers import *
from rest_framework import viewsets


class PatternCompanyViewSet(viewsets.ModelViewSet):
    queryset = PatternCompany.objects.all().order_by('company')
    serializer_class = PatternCompanySerializer


class PatternCollectionViewSet(viewsets.ModelViewSet):
    queryset = PatternCollection.objects.all().order_by('name')
    serializer_class = PatternCollectionSerializer


class PatternDesignerViewSet(viewsets.ModelViewSet):
    queryset = PatternDesigner.objects.all().order_by('name')
    serializer_class = PatternDesignerSerializer


class PatternTypeViewSet(viewsets.ModelViewSet):
    queryset = PatternType.objects.all().order_by('pattern_type')
    serializer_class = PatternTypeSerializer


class PatternViewSet(viewsets.ModelViewSet):
    queryset = Pattern.objects.all().order_by('pattern_name')
    serializer_class = PatternSerializer


class PatternViewViewSet(viewsets.ModelViewSet):
    queryset = PatternView.objects.all().order_by('view')
    serializer_class = PatternSerializer


class PatternSizeViewSet(viewsets.ModelViewSet):
    queryset = PatternSize.objects.all().order_by('size')
    serializer_class = PatternSizeSerializer


class PatternFinishedMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PatternFinishedMeasurement.objects.all().order_by('pattern_size')
    serializer_class = PatternFinishedMeasurementSerializer
