from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# from django.template import loader
# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the poll index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
