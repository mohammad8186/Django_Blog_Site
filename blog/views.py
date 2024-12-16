from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post, Comment, site_User
from .forms import CommentForm, PostForm, UserProfileForm,CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages




def home(request):

   return render(request , 'blog/home.html')



def post_list(request):
   query = request.GET.get("search")

   if query:
       posts = Post.objects.filter(Q(title__icontains=query))
   else:
        posts = Post.objects.all().order_by("-date_posted")

   context ={
        "posts":posts
    }
   
   return render (request , "blog/post_list.html" , context)
   




def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

   
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm() 

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})





@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})




@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return redirect('post_list')  

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})




@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('profile_view', username=request.user.username)
    
    return render(request, 'blog/confirm_delete.html', {'post': post})




@login_required
def profile_view(request, username):
   
    user = get_object_or_404(site_User, username=username)
    
  
    posts = Post.objects.filter(author=user)
    
  
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=user.username)
    else:
        form = UserProfileForm(instance=user)
    
    
    return render(request, 'blog/profile.html', {'user': user, 'posts': posts, 'form': form})




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid login credentials.'})
    return render(request, 'blog/login.html')




@login_required
def user_logout(request):
    logout(request)
    return redirect('post_list')




def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})