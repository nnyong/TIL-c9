from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from .forms import UserCustomCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from movies.models import Score
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method=='POST':
        user_form=UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            auth_login(request,user)
            return redirect('movies:list')
    else:
        user_form=UserCustomCreationForm()
    return render(request,'accounts/form.html',{'form':user_form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method=='POST':
        login_form=AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect('movies:list')
    else:
        login_form=AuthenticationForm()
    return render(request,'accounts/form.html',{'form':login_form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
def list(request):
    users=User.objects.all()
    return render(request,'accounts/list.html',{'users':users})

def detail(request,person_id):
    person=get_object_or_404(User,id=person_id)
    max_score=0
    recommend_movie=None
    for following in person.followings.all():
        for score in following.score_set.all():
            if score.score>max_score:
                max_score=score.score
                recommend_movie=score.movie
    return render(request,'accounts/detail.html',{'person':person,'recommend_movie':recommend_movie})
    
@login_required
def follow(request,person_id):
    person=get_object_or_404(User,id=person_id)
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:detail',person_id)
        