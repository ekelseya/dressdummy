from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Project
from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectSerializer


class PatternStashViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
