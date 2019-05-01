from django.urls import path
from . import views 

app_name='movies'

urlpatterns=[
    path('',views.list,name='list'),
    path('<int:movie_id>/',views.detail,name='detail'),
    path('<int:movie_id>/comment/new',views.comment_create,name='comment_create'),
]