#Create your views here.
from settings import *
#from itinerod.main.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.context_processors import csrf

def home(request):
  t = get_template('index.html')
  context = { 'page': 'home'}
  context.update(csrf(request))
  print str(context)
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)

def login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = auth.authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      auth.login(request, user)
      print 'logged in'
      pass
    else:
      print 'disabled account'
      pass # disabled account
  else:
    print 'invalud account, %s:%s' % (username,password)
    pass # Invalid account
  print str(request)
  return HttpResponseRedirect('/')

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/')

def signup(request):
  t = get_template('signup.html')
  context = {'page':'signup'}
  context.update(csrf(request))
  html = t.render(RequestContext(request, context))
  print "returning signup"
  return HttpResponse(html)

def adduser(request):
  print "adding user"
  print request.method
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      print "form is valid"
      new_user = form.save()
      messages.info(request, "Thanks for signing up! You are now logged in.")
      new_user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
      login(request, new_user)
      return HttpResponse(html)
    else:
      print form.get_validation_errors()
  return HttpResponseRedirect('/signup/')
