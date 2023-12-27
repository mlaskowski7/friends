from django.shortcuts import render
from .forms import PostCreateForm
# Create your views here.

def postCreateView(request):
    if request.method =='POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})
        


