from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def curtime(req):
    now= datetime.datetime.now()
    html="The time is %s" %now
    return HttpResponse(html)
def timep(req,ofs):
    a=int(ofs)
    now=datetime.datetime.now()+datetime.timedelta(hours=a)
    html="In %s hours,the time will be %s" % (a,now)
    return HttpResponse(html)
