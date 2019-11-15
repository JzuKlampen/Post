from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from Post.models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts_complete'
    template_name = 'list-post.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'post-detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
