from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Question ,Choice ,Group

def index(request):
    group_list = Group.objects.all()
    context = {'group_list': group_list}
    return render(request, 'quiz/index.html', context)

def detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'quiz/detail.html',{'group': group})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def score(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)