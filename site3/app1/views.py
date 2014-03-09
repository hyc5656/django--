from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context,Template
import datetime

# Create your views here.
def index(req):
    now=datetime.datetime.now();
    return render_to_response('index.html',{'tim':now})
