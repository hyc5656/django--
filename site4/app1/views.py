from django.shortcuts import render_to_response
from django.template import Template,Context
from app1.models import Publisher
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
#def index(req):
#    p1=Publisher.objects.all()
 
#    return render_to_response('index.html',{'p1':p1})
class usrform(forms.Form):
    name=forms.CharField(max_length=20)
    subject=forms.CharField(max_length=100)
    email=forms.EmailField(label='your email',required=False)
    message=forms.CharField(widget=forms.Textarea)
    
def index(request):
    if request.method == 'POST':
        form=usrform(request.POST)
	if form.is_valid():
	    cd=form.cleaned_data
	    return HttpResponseRedirect(r'/thanks/')
    else:
        form=usrform()
	return render_to_response('contact.html',{'f':form})

	
def thank(req):
    return HttpResponse("thanks")
