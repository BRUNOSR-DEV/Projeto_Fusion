from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import IndexView, LoginView

urlpatterns = [
    

    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'), #rota de login, necessario para logar com a rede social
    path ('logout/', auth_views.LogoutView.as_view(), name = 'logout'), #logout para desconectar 
    path('social-aut/', include('social_django.urls', namespace='social')), #necessario que ser usado os logins atráves das redes sociais
    
    path('', IndexView.as_view(), name='index'),# ('') rota para raiz - IndexView.as_view() vai ser executada como uma função
    
]
