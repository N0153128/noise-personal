from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.shortcuts import render
import constants


def main(request):
    template = loader.get_template('main/index.html')
    context = {
        'data': constants,
    }
    return HttpResponse(template.render(context, request))
