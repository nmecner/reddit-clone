from django.shortcuts import render
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        else:
            return render(request, 'accounts/signup.html', {'error': "Your passwords don't match"})

        return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')