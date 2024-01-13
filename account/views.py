from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1']== request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'account/signup.html',{'error':'Username has been already registered :( '})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password2'])
                auth.login(request,user)
                return redirect('personal')
        else:
            return render(request,'account/signup.html',{'error':'Password must match :('})
    else:

        return render(request,'account/signup.html',{})
# login view started there 
def login(request):
    #apply error handling for the login page

    try:
        if request.method=='POST':
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('personal')
            else:
                return render(request,'account/login.html',{'error':'Username or password is incorrect!'})
        else:
            return render(request,'account/login.html',{})

    except:
        if request.method=='POST':
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('personal')
            else:
                return render(request,'account/login.html',{'error':'Username or password is incorrect!'})
        else:
            return render(request,'account/login.html',{})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


#def successout(request):
#    return HttpResponse('You are Successfully Logged off')
