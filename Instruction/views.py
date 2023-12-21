from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import sys
from Agent.LLM_model import test_wrapper, gpt_wrapper
from Agent.prompts import  prompt_template_latest, repeated_attempt_template
from Agent.rubrics import rubric_dict, doktor_rubric
from .problem_statements import *
from .models import conversation



def test(request):
    return HttpResponse(test_wrapper("Hello"))

def prob1(request):
    if request.method == "POST":
        student_essay = request.POST["essay"]
        final_prompt = prompt_template_latest(student_essay = student_essay, rubric=doktor_rubric, problem_statement=ballistic_pendulum_statement) 
        print(final_prompt)
        response = gpt_wrapper(prompt = student_essay, model="gpt-4")
        return JsonResponse({"essay":student_essay,"output":response})

    context = {"problem_statement":ballistic_pendulum_statement,"rubric":rubric_dict}
    return render(request,"Instruction/ball_pendulum.html",{"context":context})

def chat(request):
    if request.method == "POST":
        ## Grab user submitting request
        USER = request.user
        USER = "m_abernathy"
        print(USER)
        
        ## Grab conversation history from database
        conversation_history = conversation.objects.filter(user=USER, problem="ballistic_pendulum")
        history = [convo.response for convo in conversation_history] 
        print(len(history))
        ## Grab student essay
        student_essay = request.POST["message"]
        print("\n".join(history))
        if history:
            final_prompt = repeated_attempt_template(history = "\n".join(history),new_attempt=student_essay)
        else:
            final_prompt = prompt_template_latest(student_essay = student_essay, rubric=doktor_rubric, problem_statement=ballistic_pendulum_statement) 
        
        response = gpt_wrapper(prompt = final_prompt)
        
        new_entry = conversation(user=USER,prompt=final_prompt,response=response, problem="ballistic_pendulum")
        new_entry.save()
        return JsonResponse({"response":response})
    else:
        context = {"problem_statement":ballistic_pendulum_statement,"rubric":rubric_dict}
        return render(request,"Instruction/UI.html",{"context":context})