# from rest_framework.generics import (
#   ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView)
from articles.models import Article
from .serializers import ArticleSerializer

# class ArticleListView(ListAPIView):
#   queryset = Article.objects.all()
#   serializer_class = ArticleSerializer

# class ArticleDetailView(RetrieveAPIView):
#   queryset = Article.objects.all()
#   serializer_class = ArticleSerializer

# class ArticleCreatelView(CreateAPIView):
#   queryset = Article.objects.all()
#   serializer_class = ArticleSerializer

# class ArticleUpdatelView(UpdateAPIView):
#   queryset = Article.objects.all()
#   serializer_class = ArticleSerializer

# class ArticleDeletelView(DestroyAPIView):
#   queryset = Article.objects.all()
#   serializer_class = ArticleSerializer

from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
  serializer_class = ArticleSerializer
  queryset = Article.objects.all()