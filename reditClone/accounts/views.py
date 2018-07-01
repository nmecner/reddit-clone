from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': "User like that already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': "Your passwords don't match"})
    else:
        return render(request, 'accounts/signup.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/login.html', {'error': 'Wrong username or password'})
    else:
        return render(request, 'accounts/login.html')