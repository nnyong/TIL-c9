from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from .forms import CustomUserCreationForm
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:list')
    if request.method=='POST':
        userform=CustomUserCreationForm(request.POST)
        if userform.is_valid():
            user=userform.save()
            auth_login(request,user)
            return redirect('accounts:list')
    else:
        userform=CustomUserCreationForm()
    return render(request,'accounts/signup.html',{'userform':userform})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:list')
    if request.method=='POST':
        loginform=AuthenticationForm(request,request.POST)
        if loginform.is_valid():
            auth_login(request,loginform.get_user())
            return redirect('accounts:list')
    else:
        loginform=AuthenticationForm()
    return render(request,'accounts/login.html',{'loginform':loginform})
    
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:list')
    
def list(request):
    users=get_user_model().objects.all()
    return render(request,'accounts/list.html',{'users':users})
    
def people(request,person_id):
    person=get_object_or_404(get_user_model(),id=person_id)
    return render(request,'accounts/people.html',{'person':person})
    
@login_required
def follow(request,person_id):
    person=get_object_or_404(get_user_model(),id=person_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:people',person_id)