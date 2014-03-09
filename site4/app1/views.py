from django.shortcuts import render_to_response
from django.template import Template,Context
from app1.models import Publisher

# Create your views here.
def index(req):
    p1=Publisher.objects.all()
 
    return render_to_response('index.html',{'p1':p1})
