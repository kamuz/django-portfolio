from django.shortcuts import render

def home(request):
    return render(request, 'base/index.html')

def posts(request):
    return render(request, 'base/posts.html')

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')
