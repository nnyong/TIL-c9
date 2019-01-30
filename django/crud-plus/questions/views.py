from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
def question(request,question_id):
    question=Question.objects.get(pk=question_id)
    return render(request,'question.html',{'question':question})