from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####

import wikipedia

# Create your views here.
def index(request):
    return HttpResponse("Hello World. You're at the wiki index.")

def get_wiki_summary(request):
    topic = request.GET.get('topic', None)
    print('Topic: ', topic)

    data = {
        'summary': wikipedia.summary(topic, sentences=1),
        'raw': 'Succesful',
    }

    print('json-data-sent: ', data)

    return JsonResponse(data)
    