from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from .models import BlogPost
from .forms import BlogPostForm

class BlogListView(LoginRequiredMixin, View):
    """
    View for displaying a list of blog posts.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        posts = BlogPost.objects.all()
        return render(request, 'blog/blog_list.html', {'posts': posts})

class BlogPostDetailView(View):
    """
    View for displaying a single blog post.
    """
    def get(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        return render(request, 'blog/blog_post.html', {'post': post})

class BlogPostCreateView(LoginRequiredMixin, View):
    """
    View for creating a new blog post.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = BlogPostForm()
        return render(request, 'blog/create_post.html', {'form': form})

    def post(self, request):
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
        return render(request, 'blog/create_post.html', {'form': form})

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    View for updating an existing blog post.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        form = BlogPostForm(instance=post)
        return render(request, 'blog/update_post.html', {'form': form, 'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post', post_id=post_id)
        return render(request, 'blog/update_post.html', {'form': form, 'post': post})

    def test_func(self):
        post = get_object_or_404(BlogPost, id=self.kwargs['post_id'])
        return self.request.user == post.author

class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    View for deleting a blog post.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        return render(request, 'blog/confirm_delete.html', {'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        post.delete()
        return redirect('blog_list')

    def test_func(self):
        post = get_object_or_404(BlogPost, id=self.kwargs['post_id'])
        return self.request.user == post.author
