from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from .forms import ScoreForm
# Create your views here.

def list(request):
    movies=Movie.objects.all()
    return render(request,'movies/list.html',{'movies':movies})
    
def detail(request,movie_id):
    movie=get_object_or_404(Movie,id=movie_id)
    scoreform=ScoreForm()
    return render(request,'movies/detail.html',{'movie':movie,'scoreform':scoreform})
    # AuthenticationForm(request,request.POST)
    # auth_login(request,user)
    # auth_login(request,user_form.get_user())

def comment_create(request,movie_id):
    scoreform=ScoreForm(request.POST)
    if scoreform.is_valid():
        score=scoreform.save(commit=False)
        score.user=request.user
        score.movie_id=movie_id
        score.save()
    return redirect('movies:detail',movie_id)
    
    