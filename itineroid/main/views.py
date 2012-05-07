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

