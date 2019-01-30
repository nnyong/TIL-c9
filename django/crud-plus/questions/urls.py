from django.urls import path
from . import views

app_name='questions'

urlpatterns = [
    path('<int:question_id>/',views.question,name='question'),
]