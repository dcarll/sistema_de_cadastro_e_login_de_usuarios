from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_auth
# Create your views here.

#rota index
def index(request):
	return render(request, 'index.html')

#criar cadastrao
def cadastro(request):
	return render(request, 'form_cadastro.html')

#rota de cadastro de usuarios
def cadastrar(request):	

	data = {}

	senha1 = request.POST.get('password')
	senha2 = request.POST.get('password2')
	name = request.POST.get('name')
	usermane = request.POST.get('user')
	email = request.POST.get('email')

	if senha1 != senha2:
		data['msg'] = 'Senha e confirmação de senha diferentes!'
		data['class'] = 'alert-danger'
	else:

		user = User.objects.create_user(username=usermane, email=email, password=senha1)
		user.first_name = name
		user.save()
		data['msg'] = 'Usuário cadastrado com sucesso!'
		data['class'] = 'alert-success'
		return redirect('login')
	return render(request, 'form_cadastro.html', data)

#login recebe o login
def login(request):
	return render(request, 'form_login.html')

#processa o login
def logar(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	data = {}
	
	user = authenticate(username=username, password=password)
	if user is not None:
		login_auth(request, user)
		return redirect('/dashboard')
	else:
		data['msg']='Senha ou usuario invalido'
		data['class']= 'alert-danger'
		return render(request, 'form_login.html', data)

	

def dashboard(request):
	return render(request, 'dashboard/home.html')
		

def logouts(request):
	logout(request)
	return redirect('index')

def change_passowrd_get(request):
	return render(request, 'form-pass.html')
		
def chenge_password(request):

	user = User.objects.get(email=request.user.email)
	senha1 = request.POST.get('password')
	senha2 = request.POST.get('password2')
	data = {}
	if senha1 != senha2:
		data['msg'] = 'Senha e confirmação de senha diferentes!'
		data['class'] = 'alert-danger'
	else:
		user.set_password(senha1)
		user.save()
		logout(request)
		return redirect('login')

	return render(request, 'form-pass.html' ,data)