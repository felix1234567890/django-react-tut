from django.db import models
from django.utils import timezone


class Article(models.Model):
    """
    Article model representing blog posts or articles in the system.

    Attributes:
        title (str): The title of the article (max 120 characters)
        content (str): The main content of the article
        created_at (datetime): When the article was created
        updated_at (datetime): When the article was last updated
    """
    title = models.CharField(max_length=120, help_text="Title of the article")
    content = models.TextField(help_text="Main content of the article")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last update timestamp")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article-detail', kwargs={'pk': self.pk})
