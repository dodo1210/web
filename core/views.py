from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from .forms import RegisterForm,CadAreaForm,ProfileForm
from .models import Perfil


def index(request):# essa view e respossavel pela chamada do index verificando se o usuario esta ou não logado 
    if not request.user.is_authenticated():#isso analisa a request e diz se o usuario esta logado isso ja é pronto do djangp
        return render(request, 'index.html')# os metodos retornado nas views são responsaveis pelo o retorno de templates html
    else:#nesse caso assima e chamado o index sem login mas cas esteja logado e chamada a view de logge que contem o perfil basico
        return HttpResponseRedirect('/loggedin/')

def login(request):#essa e apenas uma view de formulario de login
    c = {}
    c.update(csrf(request))#isso garante que o form não possa ser envadido com um form que é falso
    return render_to_response("index.html",c)#essa rederisação é algo importante para o django pois e por meio do parametro que passamos variaveis

def auth_view(request):# esse metodo é o mais importante de login
    username = request.POST.get('username','')#'teste'# aqui e pego o que está no formulario html e salvo na var de ususario
    password = request.POST.get('senha','')#'tomaz123'# aqui e pego o que está no formulario html e salvo na var de senha
    print(username)#isso é so um print comum
    user  = auth.authenticate(username=username, password=password)# essa função pronta do djanco para verificae e logar em uma conta
    if user is not None:
        auth.login(request, user)#aqui é sogado e construido a request com os dados de user
        return HttpResponseRedirect('/loggedin/')#tela de feeds chamada se der certo logui
    else:
        return render(request, 'envios.html', {'error_message': 'Invalid login'})# ususario e senhas invalidas arruamar a pagina para exibir erro


def loggedin(request):#aqui renderisa a tela com as reques de users(vai ser melhorado para ir com todas as informações)
    context = {#criação de um dicionario para questões organisacionais 
        'user' : request.user
    }
    return render_to_response('home.html',context);#renderisação de um form principal passando os dados de usuarios 

def logout(request):#essa função é pronta do django que faz logout apeans alterei o necessario
    c = {}
    c.update(csrf(request))
    auth.logout(request)
    return render_to_response('logout.html',c)

#Views direcionadas para cadastros#
def cadastro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')

    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request,'cadastro.html',context)

def perfil(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        user = request.user
        perfil = Perfil.objects.filter(user=user)
        if not perfil:
            return HttpResponseRedirect('/cadperfil/')
        else:
             return HttpResponseRedirect('/exibirPerfil/')

def cadPerfil(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                user  = request.user
                tes = form.save(commit=False)
                tes.user = user
                tes.imagem_perfil = request.FILES.get('imagem_perfil', False)
                var  = tes.imagem_perfil
                print(var)
                tes.save()
                return HttpResponseRedirect('/perfil/')
        return render(request,'Cad_Perfil.html',{'form':form})

def editarcadPerfil(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                user  = request.user
                # deve ser alterado para funcionar como um editar e não salvar form.save(user)
                return HttpResponseRedirect('/perfil/')
        return render(request,'Cad_Perfil.html',{'form':form})

def obt_Estudo(request):
    form = CadAreaForm()
    if request.method == "POST":
        form = CadAreaForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/perfil/') pensar no que fazer com essa tela de chamada aqui
    return render(request,'Cad_Areas.html',{'form':form})



#views de exibição#
def exibirPerfil(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        user = request.user
        perfil = Perfil.objects.filter(user=user)
        siglePerfil = perfil[0]
        context = {
            'perfil': siglePerfil
        }
        return render(request,'showPerfil.html',context)
