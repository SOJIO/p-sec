# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# import time

now0=datetime.datetime.now()
tip0="<html><body>now %s.</body></html>" % now0
timee="It is now"
fre=3.14

def index(request):
  now=datetime.datetime.now()
  utc=datetime.datetime.utcnow()
  today=datetime.date.today()
  time=datetime.time()
  nowh=now.hour+3

  h="<html><body>%s.</body></html>" % nowh
  m="<html><body>%s.</body></html>" % now.minute
  s="<html><body>%s.</body></html>" % now.second
  return HttpResponse("<h1 align=center> "+timee+" "+`now.year`+"|"+`now.month`+"|"+`now.day`+"  "+`nowh`+":"+`now.minute`+":"+`now.second`+" in Ukraine</h1>")

def cur_date(request):
  nw=datetime.datetime.now()
  html="<html><body>now %s.</body></html>" % nw
  return HttpResponse(html)