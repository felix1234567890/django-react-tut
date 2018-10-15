from django.urls import path
from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, base_name='articles')
urlpatterns = router.urls
# from .views import (
#   ArticleListView,ArticleDetailView, ArticleCreatelView,ArticleUpdatelView,ArticleDeletelView)

# urlpatterns = [
#   path('', ArticleListView.as_view()),
#   path('<pk>', ArticleDetailView.as_view()),
#   path('<pk>/update/', ArticleUpdatelView.as_view()),
#   path('<pk>/delete/', ArticleDeletelView.as_view()),
#   path('create/', ArticleCreatelView.as_view())
#   ]