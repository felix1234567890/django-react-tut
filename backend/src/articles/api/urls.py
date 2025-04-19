from articles.api.views import ArticleViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')

# The API URLs are determined automatically by the router
urlpatterns = router.urls

# If you need additional custom URLs, you can add them like this:
# urlpatterns += [
#     path('custom-endpoint/', custom_view, name='custom-endpoint'),
# ]