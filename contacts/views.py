from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from .models import Post
from price.models import Book
from django.http import Http404
from django.http import HttpResponse


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostListHome(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'home.html'


def error_404_view(request, exception):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')
class PostListPrice(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'price.html'

class PostListInvite(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'invite.html'


class PostListAbout(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'about.html'


class PostListJoin(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'join.html'


class PostListVacancy(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'vacancy.html'


class PostListDocs(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'docs.html'

class PostListUpload(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'upload.html'

