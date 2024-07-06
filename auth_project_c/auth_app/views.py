from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest

# Create your views here.

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def setsession(request):
    request.session['name'] = 'nauman'
    request.session['lname'] = 'ahmad'
    return render(request, 'auth_app/setsession.html')

def getsession(request):
   # name = request.session['name']
    name = request.session.get('name', default="new_user")
    lname = request.session.get('lname')
    return render(request, 'auth_app/getsession.html', {'name':name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'auth_app/delsession.html')
