from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post
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
    return render(request,'posts/feed.html',{'posts':posts})


        


