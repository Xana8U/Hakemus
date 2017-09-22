# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Hakemus/index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class QuestionsView(generic.ListView):
    template_name = 'Hakemus/questions.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'Hakemus/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'Hakemus/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'Hakemus/detail.html', {
            'question': question,
            'error_message': "Et valinnut vaihtoehtoa!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Hakemus:results', args=(question.id,)))
