from django.shortcuts import render,render_to_response,redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login(request):
    args = {}
    if request.GET:
        username = request.GET.get('username','')
        password = request.GET.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['login_error'] = "User not found"
            return render_to_response('login.html',args)
    else:
        return render_to_response('login.html', args)
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    args = {}
    args['form'] = UserCreationForm
    if request.GET:
        newuser_form = UserCreationForm(request.GET)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'],password=newuser_form.cleaned_data['password2'])
            auth.login(request,newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html',args)