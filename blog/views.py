from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

# CBV 방식
class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

# FBV 방식
# def single_post_page(request, pk):
#     post=Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )


# def index(request):
#     posts = Post.objects.all().order_by('-pk') #역순 정렬
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )
