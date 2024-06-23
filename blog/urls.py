from django.urls import path
from .views import BlogListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('post/<int:post_id>/', BlogPostDetailView.as_view(), name='blog_post'),
    path('create/', BlogPostCreateView.as_view(), name='create_post'),
    path('post/<int:post_id>/edit/', BlogPostUpdateView.as_view(), name='update_post'),
    path('post/<int:post_id>/delete/', BlogPostDeleteView.as_view(), name='delete_post'),
]
