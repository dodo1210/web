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

    #pefis e cadastros princiapais
    
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^cadperfil/$', views.cadPerfil, name='cadperfil'),
    url(r'^exibirPerfil/$', views.exibirPerfil, name='exibirPerfil'),
    url(r'^editarcadPerfil/$', views.editarcadPerfil, name='editarcadPerfil'),
    url(r'^obt_Estudo/$', views.obt_Estudo, name='obt_Estudo'),
]