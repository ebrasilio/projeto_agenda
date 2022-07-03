from django.contrib import admin
from django.urls import path, include
#from agenda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # app agendador
    path('', include('agendador.urls')),
    # app pre construido do django para conta de usuários
    #path('login/', views.login_user)
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
