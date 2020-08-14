from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *


class PatternCompanyViewSet(viewsets.ModelViewSet):
    queryset = PatternCompany.objects.all().order_by('company')
    serializer_class = PatternCompanySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternCollectionViewSet(viewsets.ModelViewSet):
    queryset = PatternCollection.objects.all().order_by('name')
    serializer_class = PatternCollectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternDesignerViewSet(viewsets.ModelViewSet):
    queryset = PatternDesigner.objects.all().order_by('name')
    serializer_class = PatternDesignerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternTypeViewSet(viewsets.ModelViewSet):
    queryset = PatternType.objects.all().order_by('pattern_type')
    serializer_class = PatternTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternViewSet(viewsets.ModelViewSet):
    queryset = Pattern.objects.all().order_by('pattern_name')
    serializer_class = PatternSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternViewViewSet(viewsets.ModelViewSet):
    queryset = PatternView.objects.all().order_by('view')
    serializer_class = PatternSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternSizeViewSet(viewsets.ModelViewSet):
    queryset = PatternSize.objects.all().order_by('size')
    serializer_class = PatternSizeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PatternFinishedMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PatternFinishedMeasurement.objects.all().order_by('pattern_size')
    serializer_class = PatternFinishedMeasurementSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
