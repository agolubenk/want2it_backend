from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from .forms import CommentForm
from vacancy.models import Vacancy
from contacts.models import Contact
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def blog_list(request):
    """Формирует список статей"""
    posts = Blog.objects.filter(draft=1).order_by('-blog_date')
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    vacancys = Vacancy.objects.filter(hot=1).order_by('-vacancy_date')
    contacts = Contact.objects.filter(title='Организация')
    return render(request, 'blog/list.html', {'posts': posts, 'menuposts': menuposts, 'vacancys': vacancys, 'contacts': contacts})


def blog_detail(request, pk):
    """Формирует отдельную статью и список"""
    post = get_object_or_404(Blog, pk=pk)
    lastposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:5]
    menuposts = Blog.objects.filter(draft=1).order_by('-blog_date')[:3]
    contacts = Contact.objects.filter(title='Организация')
    comments = post.comments.filter(status=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'menuposts': menuposts, 'contacts': contacts, 'lastposts': lastposts,'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

