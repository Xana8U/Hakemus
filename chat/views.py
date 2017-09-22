# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import send, feed
from django.urls import reverse
from django.views import generic
from django.shortcuts import render


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    #context_object_name = 'latest_send_list'

    def get_queryset(self):
        return feed.objects.order_by('id')[:5]


class SendView(generic.ListView):
    template_name = 'chat/messages.html'
    context_object_name = 'latest_send_list'

    def get_queryset(self):
        return send.objects.all()


class LogView(generic.ListView):
    template_name = 'chat/log.html'
    context_object_name = 'latest_send_list'

    def get_queryset(self):
        return send.objects.all()


def add(request):
    if request.method == "POST":

        if True:
            saved_username = request.POST.get("user")
            saved_message = request.POST.get("message")
            msg_send = send(sender=saved_username, message=saved_message)
            msg_send.save()
        return HttpResponseRedirect(reverse('chat:index'))
    else:
        raise Http404

