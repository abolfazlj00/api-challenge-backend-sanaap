from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.select_related("owner").all()
    serializer_class = DocumentSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Automatically assign the logged-in user
