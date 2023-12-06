from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import sys
from Agent.LLM_model import test_wrapper
from Agent.prompts import prompt_template
from Agent.rubrics import rubric_dict
from .problem_statements import *



def test(request):
    return HttpResponse(test_wrapper("Hello"))

def prob1(request):
    if request.method == "POST":
        student_essay = request.POST["essay"] 
        response = test_wrapper(student_essay)
        print(response)
        return JsonResponse({"essay":student_essay,"output":response})

    context = {"problem_statement":ballistic_pendulum_statement,"rubric":rubric_dict}
    return render(request,"Instruction/ball_pendulum.html",{"context":context})