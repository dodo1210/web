# -*- coding: utf 8 -*-
from django.shortcuts import render,render_to_response,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from .forms import RegisterForm,CadAreaForm,ProfileForm,CadGrupForm,Obt_Estudo,FormPublicacao_Grupo_de_Estudo,FormComent_Publicacao_Grupo_de_Estudo
from .models import User,Perfil,Obt_Estudo,Publicacao,Coment_Publi,Forum_Duvida,Resp_Forum_Duvida,Grupo_de_Estudo,Publicacao_Grupo_de_Estudo,Coment_Publicacao_Grupo_de_Estudo,Seguidor

from .models import Forum_Duvida as Forum_duvidas
from .models import Publicacao as Publicacaos
from .models import Grupo_de_Estudo as Grupos
from .models import Coment_Publi as Coment_Publis
from .models import Resp_Forum_Duvida as Resp_Forum_Duvidas
from .models import Perfil as Perfils
from .models import Publicacao_Grupo_de_Estudo as Publicacao_Grupo_de_Estudos
from .models import Coment_Publicacao_Grupo_de_Estudo as  Coment_Publicacao_Grupo_de_Estudos

from .forms import Forum_Duvida, Publicacao, RegisterForm,Edit_User, Coment_Publi, Resp_Forum_Duvida

from django.utils import timezone
from datetime import datetime

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
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        user = request.user
        perfil1 = Perfil.objects.filter(user=user)
        if perfil1:
            aux = perfil1[0]
        else:
            aux = Perfil()
            
        context = {#criação de um dicionario para questões organisacionais 
            'user' : request.user,
            'perfil': aux
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
    bus = request.POST.get('busca')
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
                print(tes.user)
                tes.imagem_perfil = request.FILES.get('imagem_perfil', False)
                var  = tes.imagem_perfil
                print(var)
                tes.save()
                return HttpResponseRedirect('/exibirPerfil/')
        return render(request,'Cad_Perfil.html',{'form':form})

def editarcadPerfil(request):
    user = request.user.id
    perfil1 = Perfil.objects.filter(user=user)
    aux = perfil1[0]
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        perfil = Perfil.objects.get(id=aux.id)
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                perfil.data_altera = datetime.now()
                tes = request.FILES.get('imagem_perfil', False)
                if request.POST.get('bio'):
                    perfil.bio = request.POST.get('bio')
                if tes:
                    perfil.imagem_perfil = tes
                #por o save nesse local do codigo
                perfil.save()
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

def cadGrupoDeestuds(request):
    user = request.user
    form = CadGrupForm()
    perfil = Perfil.objects.filter(user=user)
    perfil1 = perfil[0]
    if request.method == "POST":
        form = CadGrupForm(request.POST)
        if form.is_valid():
            area = get_object_or_404(Obt_Estudo,id=request.POST.get('area',''))
            aux = form.save(commit=False)
            aux.user_adm = perfil1
            aux.imagem_logo = request.FILES.get('imagem_logo', False)
            aux.save()
            aux.area.add(area)
            aux.participantes.add(request.user)
    context = {
        'perfil' : Perfils.objects.get(id=request.user.id),
        'form': form
    }
    return render(request,'criarGrupo.html',context)


#views de exibição#
#def exibirPerfil(request):
#    if not request.user.is_authenticated():
#        return render(request, 'index.html')
#    else:
#        user = request.user
#        perfil = Perfil.objects.filter(user=user)
#        siglePerfil = perfil[0]
#        context = {
#            'perfil': siglePerfil
#        }
#        return render(request,'showPerfil.html',context)


def showGrupo(request):#usar o metodos de pegar as os dados tranforma em lista e utilisar para comparação
    grupos  = Grupo_de_Estudo.objects.all()
    allGrups = []
    for grupo in grupos:
        listauser = list(grupo.participantes.all())
        if request.user in listauser:
            allGrups.append(grupo)

    context = {
        'grupos':allGrups
    }

    return render(request,"grupos.html",context)


def showSingleGupo(request,id):
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        grupo = Grupo_de_Estudo.objects.get(id=id)
        if request.method == "POST":
            form = FormPublicacao_Grupo_de_Estudo(request.POST)
            if form.is_valid():
                user  = request.user
                perfil = Perfil.objects.filter(user=user)
                perfil1 = perfil[0]
                area = get_object_or_404(Obt_Estudo,id=request.POST.get('area',''))
                publicate = form.save(commit=False)
                publicate.anexo = request.FILES.get('anexo', False)
                publicate.user = user
                publicate.grupo = grupo
                publicate.perfil = perfil1
                publicate.save()
                publicate.area.add(area)
        postes = Publicacao_Grupo_de_Estudo.objects.filter(grupo=grupo)
        form = FormPublicacao_Grupo_de_Estudo()
        context = {
            'grupo': grupo,
            'form' : form,
            'post' :postes,
            'publis' : postes
        }
        return render(request,'grupo.html',context)



def showSinglePublicateGrupo(request,id):
    publicate = Publicacao_Grupo_de_Estudos.objects.get(id=id)
    print (publicate.titulo)
    if request.method == "POST":
            form = FormComent_Publicacao_Grupo_de_Estudo(request.POST)
            if form.is_valid():
                print ("werw")
                user  = request.user
                perfil = Perfil.objects.filter(user=user)
                perfil1 = perfil[0]
                grupo = publicate.grupo
                comentario = form.save(commit=False)
                comentario.user = user
                comentario.perfil = perfil1
                comentario.publi = publicate
                comentario.grupo = grupo
                comentario.save()
    coment = Coment_Publicacao_Grupo_de_Estudos.objects.filter(publi=publicate).order_by('-pk')
    form =  FormComent_Publicacao_Grupo_de_Estudo()
    context = {
            'publicacao': publicate,
            'form' : form,
            'coments' :coment,
            'grupo' : Grupos.objects.get(id = id),
    }
    return render(request,'showPublicate.html',context)

#douglas

def home(request):
    
    form = Publicacao(request.POST, request.FILES)
    publicacaos = None

    context = {
        'user' : request.user,
        'form' : form,
        'publicacao' : Publicacaos.objects.all().order_by('-pk')
    }

    bus = request.POST.get('busca')
    if request.method == 'POST' and form.is_valid():
        publicacaos = form.save(commit=False)
        publicacaos.anexo = request.FILES.get('anexo', False)
        publicacaos.user = request.user
        publicacaos.save()
        return render(request,'home.html',context)
    return render(request,'home.html',context)

def viewPublicacao(request,publicacao_id):

    form = Coment_Publi(request.POST or None)
    publi = Publicacaos.objects.get(id=publicacao_id)
    comentarios = Coment_Publis.objects.filter(publi=publi).order_by('-pk')

    context = {
        'user' : request.user,
        'form' : form,
        'publicacao' : publi,
        'comentarios' : comentarios
    }

    if request.method == 'POST':
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = request.user
            comentario.publi_id = publicacao_id
            comentario.save()
            return HttpResponseRedirect('/viewPublicacao/'+publicacao_id)
    return render(request,'viewPublicacao.html',context)

def seu_grupo(request):
    bus = request.POST.get('busca')

    context = {
        'user' : request.user,
        'grupos' : Grupos.objects.all(),
        'seu_grupo' : Grupos.objects.filter(participantes = request.user),
    }

    return render(request,'seu_grupo.html',context)

def grupo(request):
    bus = request.POST.get('busca')
    return render(request,'grupo.html')

def forum(request):
    perfil = Perfils.objects.filter(user=request.user)
    if perfil:
        perfil1 = perfil[0]
    else:
       perfil1 = Perfil() 
    context = {
        'user' : request.user,
        'foruns':Forum_duvidas.objects.filter(user=request.user).order_by('-pk'),
        'perfil':perfil1
    }

    form = Forum_Duvida(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user
            forum.save()
            return HttpResponseRedirect('/forum/')
    return render(request,'forum.html',context)

def editForum(request,forum_id):
    perfil = Perfils.objects.filter(user=request.user)
    if perfil:
        perfil1 = perfil[0]
    else:
       perfil1 = Perfil()
    context = {
        'user' : request.user,
        'forum':Forum_duvidas.objects.get(id=forum_id),
        'perfil': perfil1
    }

    form = Forum_Duvida(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            forum = form.save(commit=False)
            forum.id = forum_id
            forum.user = request.user
            forum.texto = request.POST.get('texto')
            forum.area.id = request.POST.get('area')
            forum.save()
            return HttpResponseRedirect('/forum/')
    return render(request,'editForum.html',context)

def pergunta_forum(request,forum_id):

    forum = Forum_duvidas.objects.get(id=forum_id)
    teste = Resp_Forum_Duvidas.objects.filter(forum=forum)
    context = {
        'user' : request.user,
        'forum':Forum_duvidas.objects.get(id=forum_id),
        'usuario_publicou' : forum.user.username,
        'respostas' : Resp_Forum_Duvidas.objects.filter(forum = forum).order_by('-pk')
    }

    form = Resp_Forum_Duvida(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            resp_forum = form.save(commit=False)
            resp_forum.user = request.user
            resp_forum.forum = forum
            resp_forum.save()
            return HttpResponseRedirect('/pergunta_forum/'+forum_id)
    return render(request,'pergunta_forum.html',context)

def materia(request):
    return render(request,'materia.html')

def buscar(request):
    
    bus = str(request)
    #pega apenas a parte que interesa da request
    busca = ""
    i = 0
    for b in bus:
        if b == '=':
            i=1
        if b == '>':
            i = 0
        if i==1:
            busca=str(busca)+str(b)
    buscar = ""
    
    bus = request.POST.get('busca')
    #inserir em buscar apenas o que interesa com a '
    for i in range(len(busca)-1):
        buscar=buscar+busca[i+1]
    busca = ""
    #retira a aspa simples
    for i in range(len(buscar)-1):
        busca=busca+buscar[i]
    print(busca)

    context = {
        'user' : request.user,
        'perfil' : Perfils.objects.get(id=request.user.id),
        
        'usuarios' : User.objects.filter(username = busca),
        'grupos' : Grupos.objects.filter(titulo = busca),
        'foruns' : Forum_duvidas.objects.filter(texto=busca),
        'publicacaos' : Publicacaos.objects.filter(titulo=busca),
        
        'tam_usuarios' : len(User.objects.filter(username=busca)),
        'tam_grupos' : len(Grupos.objects.filter(titulo=busca)),
        'tam_foruns' : len(Forum_duvidas.objects.filter(texto=busca)),
        'tam_publicacoes' : len(Publicacaos.objects.filter(titulo=busca)),
        
        'buscar' : busca
    }
    return render(request,'buscar.html',context)

def editar_usuario(request):
    form = RegisterForm(request.POST)
    form1 = Edit_User(request.POST or None)
    print (request.user.id)
    user = User.objects.get(id=request.user.id)
    bus = request.POST.get('busca')
    context = {
        'user' : request.user,
        'form' : form,
        'form1' : form1
    }
    
    if request.method == 'POST':
        if form1.is_valid():
            user.id = request.user.id
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            return render(request,'editar_usuario.html')
    return render(request,'editar_usuario.html',context)

def exibirPerfil(request):
    
    bus = request.POST.get('busca')
    context = {
        'user' : request.user,
        'publicacao' : Publicacaos.objects.filter(user=request.user).order_by('-pk')
    }

    if not request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        user = request.user
        perfil = Perfil.objects.filter(user=user)
        if not perfil:
            return HttpResponseRedirect('/cadperfil/')
        else:
            return render(request,'perfil.html',context)

def showPerfil(request,perfil_id):
    
    usuario = User.objects.get(id=perfil_id);
    bus = request.POST.get('busca')
    context = {
        'user' : request.user,
        'usuario' : usuario,
        'publicacoes' : Publicacaos.objects.filter(user=usuario).order_by('-pk')
    }
    return render(request,'showPerfil.html',context)

#def editarcadPerfil(request):
   
#    form = ProfileForm(request.POST,request.FILES)
#    context = {
#        'form' : form,
#        'perfil' : Perfils.objects.get(id=request.user.id)
#    }
#
#    if not request.user.is_authenticated():
#        return render(request, 'index.html')
#    else:
#        if request.method == "POST":
#            form = ProfileForm(request.POST)
#            if form.is_valid():
#                perfil = form.save(commit=False)
#                perfil.id = request.user.id
#                perfil.imagem_perfil = request.FILES.get('anexo', False)
#                perfil.user = request.user
#                perfil.save()
#                return HttpResponseRedirect('/perfil/')
#        return render(request,'Cad_Perfil.html',context)

def obt_Estudo(request):
    form = CadAreaForm()
    if request.method == "POST":
        form = CadAreaForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/perfil/') pensar no que fazer com essa tela de chamada aqui
    return render(request,'Cad_Areas.html',{'form':form})

#def exibirPerfil(request):
#    if not request.user.is_authenticated():
#        return render(request, 'index.html')
#    else:
#        user = request.user
#        perfil = Perfil.objects.filter(user=user)
#        siglePerfil = perfil[0]
#        context = {
#            'perfil': siglePerfil
#        }
#        return render(request,'showPerfil.html',context)


def editPublicacoes(request,publicacao_id):

    form = Publicacao(request.POST, request.FILES)
    bus = request.POST.get('busca')
    context = {
        'user' : request.user,
        'form' : form,
        'publicacao' : Publicacaos.objects.get(id=publicacao_id),
        'perfil' : Perfils.objects.get(id=request.user.id)
    }

    p = Publicacaos.objects.get(id=publicacao_id)

    if request.method == 'POST' and form.is_valid():
        publicacaos = form.save(commit=False)
        publicacaos.id = publicacao_id
        publicacaos.anexo = p.anexo
        publicacaos.user = request.user
        publicacaos.titulo = request.POST.get('titulo')
        publicacaos.texto = request.POST.get('texto')
        print (request.POST.get('area'))
        publicacaos.area.id = request.POST.get('area')
        publicacaos.save()
        return HttpResponseRedirect('/exibirPerfil/')
    return render(request,'editPublicacoes.html',context)

def removePublicacoes(request,publicacao_id):

    form = Publicacao(request.POST, request.FILES)
    bus = request.POST.get('busca')
    context = {
        'user' : request.user,
    }

    if request.method == 'POST':
        Publicacaos.objects.get(id=publicacao_id).delete()
        return HttpResponseRedirect('/exibirPerfil/')
    return render(request,'removePublicacao.html',context)  