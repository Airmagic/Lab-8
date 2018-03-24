from django.shortcuts import render
# added this to get utilities
from django.utils import timezone
# added this to access post
from .models import Post

# Create your views here.
# this will render the template
def post_list(request):
    # this is for posting
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
