# -*- coding: utf 8 -*-
from django.conf.urls import url

from . import views
#from django.contrib.auth import views

urlpatterns = [
    #autenticação e login
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login_user'),
    url(r'^auth/$',views.auth_view , name='auth'),
    url(r'^logout/$', views.logout, name='logout_user'),
    url(r'^loggedin/$', views.loggedin, name='logged'),
    url(r'^register/$', views.cadastro, name='register'),
    url(r'^home/$', views.home, name='home'),

    #pefis e cadastros princiapais
    url(r'^edit_user/$', views.editar_usuario, name='editar_usuario'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^cadperfil/$', views.cadPerfil, name='cadperfil'),
    url(r'^editarcadPerfil/$', views.editarcadPerfil, name='editarcadPerfil'),
    url(r'^showPerfil/(?P<perfil_id>\d+)/$', views.showPerfil, name='showPerfil'),
    url(r'^obt_Estudo/$', views.obt_Estudo, name='obt_Estudo'),
    url(r'^exibirPerfil/$', views.perfil, name='exibirPerfil'),
    url(r'^exibirSelfPerfil/$', views.exibirPerfil, name='exibirselfPerfil'),

    #grupos de estudos
    url(r'^grupo/$', views.showGrupo, name='grupo'),
    url(r'^criarGrupos/$', views.cadGrupoDeestuds, name='grupos'),
    url(r'^grupo/(?P<id>\d+)/$', views.showSingleGupo, name='gruposSingle'),
    url(r'^pucacaogrupo/(?P<id>\d+)/$', views.showSinglePublicateGrupo, name='showSinglePublicateGrupo'),
    url(r'^seu_grupo/$', views.showGrupo, name='seu_grupo'),
    url(r'^participaGrupo/(?P<id>\d+)/$', views.participatedGrupo, name='participatedGrupo'),
    url(r'^sair/(?P<id>\d+)/$', views.sairGrupo, name='sairGrupo'),
    url(r'^deletar/(?P<id>\d+)/$', views.excluirGrupo, name='excluirGrupo'),
    url(r'^editar/(?P<id>\d+)/$', views.editarGrupo, name='editarGrupo'),
    url(r'^deletComentPost/(?P<id>\d+)/$', views.deletComentPost, name='deletComentPost'),
    url(r'^deletPublicGrupo/(?P<id>\d+)/$', views.deletPublicGrupo, name='deletPublicGrupo'),
    url(r'^editPublicGrupo/(?P<id>\d+)/$', views.editPublicGrupo, name='editPublicGrupo'),
    
    #forum e busca
    url(r'^forum/$', views.forum, name='forum'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^pergunta_forum/(?P<forum_id>\d+)$', views.pergunta_forum, name='pergunta_forum'),
    url(r'^editForum/(?P<forum_id>\d+)/$', views.editForum, name='editForum'),
    
    #publicação
    url(r'^editarPublicacoes/(?P<publicacao_id>\d+)/$', views.editPublicacoes, name='editarPublicacoes'),
    url(r'^excluirPublicacoes/(?P<publicacao_id>\d+)/$', views.removePublicacoes, name='excluir'),
    url(r'^viewPublicacao/(?P<publicacao_id>\d+)/$', views.viewPublicacao, name='viewPublicacao'),
    url(r'^deletComent/(?P<publicacao_id>\d+)/$', views.deletComent, name='deletComent'),

    #seguirdores 
    url(r'^seguir/(?P<id>\d+)/$', views.seguir, name='seguir'),
    url(r'^deixarseguir/(?P<id>\d+)/$', views.deixarseguir, name='deixarseguir'),
    url(r'^seguindo/$', views.seguindo, name='seguindo'),
    url(r'^seguidores/$', views.seguidores, name='seguidores'),
]
