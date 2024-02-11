from django.contrib import admin
from django.urls import path, include
from . import views
from Agent.rubrics import doktor_rubric
from Agent.prompts import prompt_template_latest, repeated_attempt_template
from .problem_statements import *

ball_pend_args = {"rubric": doktor_rubric, 
                  "problem_statement": ballistic_pendulum_statement, 
                  "prompt": prompt_template_latest, 
                  "problem": "ballistic_pendulum"}

app_name = 'Instruction'
urlpatterns = [
    path('test/',views.test, name='test'),
    path('chat/',views.chat, name='chat',kwargs=ball_pend_args)
]