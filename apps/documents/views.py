from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.pagination import PageNumberPagination
from .models import Document
from .serializers import DocumentSerializer

class DocumentPagination(PageNumberPagination):
    page_size = 20  # documents per page
    page_size_query_param = 'page_size'  # allow client to override
    max_page_size = 100

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.select_related("owner").all()
    serializer_class = DocumentSerializer
    permission_classes = [DjangoModelPermissions]
    pagination_class = DocumentPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'owner__username']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
