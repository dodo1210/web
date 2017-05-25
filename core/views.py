from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib import auth
from django.template.context_processors import csrf

def index(request):
	return render(request,"index.html")

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html",c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('senha','')
    user  = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'index.html', {'error_message': 'Invalid login'})





    """if request.method == "POST":
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
            """