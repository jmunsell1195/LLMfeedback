from django.shortcuts import redirect, render
from django.http import HttpResponse
import sys
from Agent.LLM_model import test_wrapper

def test(request):
    return HttpResponse(test_wrapper("Hello"))