from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Project
from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('pattern', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
