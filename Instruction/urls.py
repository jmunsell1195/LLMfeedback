from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Instruction'
urlpatterns = [
    path('test/',views.test, name='test'),
    path('chat/',views.chat, name='chat'),
    path('problem1/',views.prob1, name="prob1")
]