from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),

    # depois de logado
    path('listar/', views.listar, name='listar_evento'),
    #crud
    path('agendar/', views.agendar, name='novo_evento'),
    path('update/<int:pk>/', views.update, name='url_update'),
    path('delete/<int:pk>/', views.delete, name='url_delete'),
    path('cadastro_cliente/',views.cadastro_cliente, name='url_novocliente'),
    
    # auth login
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('login/submit', views.submit_login, name='submit_login'),

    
]
