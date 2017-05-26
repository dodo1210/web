from django.conf.urls import url

from . import views
#from django.contrib.auth import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login_user'),
    url(r'^auth/$',views.auth_view , name='auth'),
    url(r'^logout/$', views.logout, name='logout_user'),
    url(r'^loggedin/$', views.loggedin, name='logged'),
] 