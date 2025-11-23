from django.urls import path
from quizapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nextpage', views.nextpage, name= 'nextpage')
]