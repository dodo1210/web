from django.conf.urls import url

from . import views
#from django.contrib.auth import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login_user'),
    #url(r'^login/$', views.login, {'template_name': 'index.html'}, name='login')
] 