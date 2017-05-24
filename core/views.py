from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
	return render(request,"index.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('senha')     
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'index.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'index.html', {'error_message': 'Invalid login'})
    return render(request, 'index.html')
