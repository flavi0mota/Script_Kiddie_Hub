from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        context['comment-form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

# Create your views here.
def index(request):
    return HttpResponse("If you're seeing this, it's the first commit")