from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # app agendador
    path('', include('agendador.urls')),
    # app pre construido do django para conta de usuários
    path('accounts/', include('django.contrib.auth.urls')),

]
