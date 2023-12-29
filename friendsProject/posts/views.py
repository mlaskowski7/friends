from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404, redirect
# Create your views here.


@login_required
def postCreateView(request):
    if request.method =='POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request,'posts/createPost.html',{'form':form})

@login_required
def feedView(request):
    posts = Post.objects.all()
    logged_user = request.user
    return render(request,'posts/feed.html',{'posts':posts, 'logged_user':logged_user})

@login_required
def like_postView(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post,id=post_id)
    if post.liked_by.filter(id=request.user.id):
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user);
    return redirect('feed')

        


