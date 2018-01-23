from django.shortcuts import render, get_object_or_404

from .models import Posts
from .forms import PostsForm
# Create your views here.

def index(request):

    posts = Posts.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "index.html", context)

def create(request):

    form = PostsForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
        "title": "Post create",
    }

    return render(request, "create.html", context)

def read(request, id):

    posts = Posts.objects.get(id=id)

    context = {
        "posts": posts
    }

    return render(request, "read.html", context)

def delete(request, id):

    posts = Posts.objects.get(id=id).delete()



    return render(request, "delete.html")


def edit(request, id):

    instance = get_object_or_404(Posts, id=id)

    form = PostsForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context={
        "form": form,
        "title": "Edit Post"
    }

    return render(request, 'create.html', context)

##remaining edit
