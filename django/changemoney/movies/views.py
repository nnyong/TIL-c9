from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie,Score
from .forms import ScoreForm,MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def list(request):
    movies=Movie.objects.all()
    return render(request,'movies/list.html',{'movies':movies})
    
def new(request):
    movieform=MovieForm()
    return render(request,'movies/form.html',{'movieform':movieform})
    
def detail(request,movie_id):
    movie=get_object_or_404(Movie,id=movie_id)
    scoreform=ScoreForm()
    return render(request,'movies/detail.html',{'movie':movie,'scoreform':scoreform})
    
def delete(request,movie_id):
    movie=get_object_or_404(Movie,id=movie_id)
    movie.delete()
    return redirect('movies:list')
    
@login_required
def score_new(request,movie_id):
    scoreform=ScoreForm(request.POST)
    if scoreform.is_valid():
        score=scoreform.save(commit=False)
        score.movie_id=movie_id
        score.user=request.user
        score.save()
    return redirect('movies:detail', movie_id) 

@login_required
def score_delete(request,movie_id,score_id):
    score=get_object_or_404(Score,id=score_id)
    if request.user==score.user:
        score.delete()
    return redirect('movies:detail',movie_id)