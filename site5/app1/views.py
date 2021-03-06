from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from app1.models import User

# Create your views here.
class uform(forms.Form):
    username=forms.CharField(max_length=30)
    img=forms.FileField()

def reg(req):
    if req.method=='POST':
        uf=uform(req.POST,req.FILES)
	if uf.is_valid():
	    user=User()
	    user.username=uf.cleaned_data['username']
	    user.img=uf.cleaned_data['img']
	    user.save()
	    req.session['usr']=user.username
	    return HttpResponseRedirect(r'/success/')
        else :
	    return render_to_response('register.html',{'f':uf})
    else:
        uf=uform()
	return render_to_response('register.html',{'f':uf})

def suc(req):
    username=req.session['usr']
    return render_to_response('success.html',{'username':username})

def logout(req):
    del req.session['usr']
    return HttpResponse("logout!!")
