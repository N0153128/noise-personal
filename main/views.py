from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import *
import constants


def main(request):
    template = loader.get_template('main/index.html')
    context = {
     }
    return HttpResponse(template.render(context, request))


def person(request, pk):
    person_data = Person.objects.get(id=pk)
    template = loader.get_template('main/person.html')
    context = {
        'person': person_data,
        'data': constants,
    }
    return HttpResponse(template.render(context, request))


def author(request):
    person_data = Person.objects.get(id=1)
    posts = Post.objects.filter(post_author__id=1)
    template = loader.get_template('main/person.html')
    context = {
        'person': person_data,
        'data': constants,
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('main/about.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
