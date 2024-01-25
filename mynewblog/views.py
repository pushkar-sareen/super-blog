from django.shortcuts import render, redirect
from mynewblog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def landing_page(request):
    rock = Post.objects.filter(post_catrgory="rock")
    jazz = Post.objects.filter(post_catrgory="jazz")
    electronic = Post.objects.filter(post_catrgory="electronic")
    context = {'posts_rock': rock,
               'posts_jazz':jazz,
               'posts_electronic':electronic
               }
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')
def blog_post(request):
    if request.method == 'POST':
        post_title = request.POST.get('post_title')
        post_description = request.POST.get('post_description')
        post_category = request.POST.get('post_category')
        Post.objects.create(post_title=post_title, post_description=post_description, post_catrgory=post_category)
        return redirect('/')
    queryset = Post.objects.all()
    context = {'posts': queryset}
    return render(request, 'form.html', context)


def post_delete(request, id):
    queryset = Post.objects.get(id=id)
    queryset.delete()
    return redirect('/form-data/')



def post_update(request, id):
    queryset = Post.objects.get(id=id)
    if request.method == 'POST':
        post_title = request.POST.get('post_title')
        post_description = request.POST.get('post_description')
        post_category = request.POST.get('post_category')
        queryset.post_title= post_title
        queryset.post_description= post_description
        queryset.post_catrgory= post_category
        queryset.save()
        return redirect('/')

    context = {'post': queryset}
    return render(request, 'update.html', context)