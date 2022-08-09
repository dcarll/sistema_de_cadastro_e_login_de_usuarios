from django.urls import path
from .views import index, cadastrar, cadastro, login, logar, dashboard, logouts, chenge_password, change_passowrd_get

urlpatterns = [
	path('', index, name='index'),
	path('cadastro/', cadastro, name='cadastro'),
	path('cadastrar/', cadastrar, name='cadastrar'),
	path('login/', login, name='login'),
	path('logar/', logar, name='logar'),
	path('dashboard/', dashboard, name='dashboard'),
	path('logouts/', logouts, name='logout'),
	path('mudar-senha/', change_passowrd_get),
	path('alteracao-de-senha/', chenge_password),


]