from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import PatternStash, FabricStash
from .permissions import IsOwnerOrReadOnly
from .serializers import PatternStashSerializer, FabricStashSerializer


class PatternStashViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PatternStashSerializer
    queryset = PatternStash.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FabricStashViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = FabricStashSerializer
    queryset = FabricStash.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
