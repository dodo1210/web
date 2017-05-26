from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserForm
from django.contrib import auth
from django.template.context_processors import csrf




def index(request):
    return render(request,"envios.html")

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("index.html",c)

def auth_view(request):
    username = request.POST.get('username','')#'teste'#
    password = request.POST.get('senha','')#'tomaz123'#
    print(username)
    user  = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return render(request, 'envios.html', {'error_message': 'Invalid login'})


def loggedin(request):
    context = {
        'user' : request.user
    }
    return render_to_response('home.html',context);

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def cadastro(request):
    if request.method == "POST":
        print("Teste")
    context = {
        'form' : auth.forms.UserCreationForm()
    }
    return render(request,'cadastro.html',context)
