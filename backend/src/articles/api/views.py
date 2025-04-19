from articles.models import Article
from django.db.models import Q
from rest_framework import filters, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing articles.

    Provides CRUD operations for Article objects.

    list:        GET /api/
    retrieve:    GET /api/{id}/
    create:      POST /api/
    update:      PUT /api/{id}/
    partial_update: PATCH /api/{id}/
    destroy:     DELETE /api/{id}/
    search:      GET /api/search/?q={query}
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]  # Can be changed to IsAuthenticated if needed
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']  # Default ordering

    def get_queryset(self):
        """
        Optionally restricts the returned articles,
        by filtering against query parameters in the URL.
        """
        queryset = Article.objects.all()
        # Example of how to filter by query parameters
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Custom search endpoint that searches both title and content.

        Example: GET /api/search/?q=django
        """
        query = request.query_params.get('q', '')
        if query:
            queryset = self.queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response([])