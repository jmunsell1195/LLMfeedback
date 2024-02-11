from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import sys

from Agent.rubrics import doktor_rubric
from Agent.prompts import prompt_template_latest, repeated_attempt_template
from .problem_statements import *
from Agent.LLM_model import gpt_wrapper
from .problem_statements import *
from .models import conversation


def test(request):
    return HttpResponse(test_wrapper("Hello"))


def chat(request, rubric, problem_statement, prompt, problem):
    if request.method == "POST":
        ## Grab name of user submitting request
        USER = request.user
        USER = "f_smith"
        print(USER)

        ## Grab conversation history from database
        conversation_history = conversation.objects.filter(user=USER, problem=problem)
        response_history = [convo.response for convo in conversation_history]
        essay_history = [convo.response for convo in conversation_history]
        print(len(response_history))

        ## Grab student essay
        student_essay = request.POST["message"]
        print(len("\n".join(essay_history)))

        ## if student has submitted an essay previously
        if essay_history:
            chat_history = ""
            for essay, reponse in zip(essay_history, response_history):
                chat_history += f"{prompt(problem_statement=ballistic_pendulum_statement,student_essay=essay,rubric=doktor_rubric)}"
            final_prompt = repeated_attempt_template(
                history=chat_history, new_attempt=student_essay
            )

        ## else submit a first request
        else:
            final_prompt = prompt(
                student_essay=student_essay,
                rubric=doktor_rubric,
                problem_statement=ballistic_pendulum_statement,
            )

        response = gpt_wrapper(prompt=final_prompt)

        new_entry = conversation(
            user=USER,
            essay=student_essay,
            response=response,
            problem="ballistic_pendulum",
        )
        new_entry.save()
        return JsonResponse({"response": response})

    else:
        rubric = rubric.split("#")[1:]
        rubric_dict = dict(
            zip(
                [row.split(":")[0].split("(")[0] for row in rubric],
                [row.split(":")[1].strip() for row in rubric],
            )
        )
        context = {
            "problem_statement": ballistic_pendulum_statement,
            "rubric": rubric_dict,
        }
        return render(request, "Instruction/UI.html", {"context": context})
