from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        if not username:
            return render(request, 'index.html', {'error': 'Username cannot be empty'})
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'index.html', {'error': 'Username already exists'})
        else:
            my_user = User.objects.create_user(username)
            my_user.save()
            return render(request,'nextpage.html', {'user': username})
    return render(request, 'index.html')
def nextpage(request):
    return render(request, 'nextpage.html')