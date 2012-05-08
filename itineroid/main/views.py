
#Create your views here.
from settings import *
#from itinerod.main.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from main.models import UserProfile, Itinerary, Location, Activity

def home(request):
  t = get_template('index.html')
  context = { 'page': 'home'}
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)

def profile(request):
    user_profile = UserProfile.objects.get(pk=1)
    return render_to_response('profile.html', {'profile' : user_profile})

# TODO check that user has authorization to view current itinerary

def itinerary(request):
    try:
        selected_itinerary = Itinerary.objects.get(pk=request.GET['id'])
    except (KeyError, Itinerary.DoesNotExist):
        # fix this later
        raise Http404
    return render_to_response('itinerary.html', {'itinerary' : selected_itinerary })

def itineraryadd(request):
    try:    
        userprofile=UserProfile.objects.get(pk=request.GET['profileid'])
        itinerary_name=request.GET['name']
        location_name=request.GET['location']
        start=request.GET['start']
        end=request.GET['end']
    except (KeyError, UserProfile.DoesNotExist): 
        raise Http404

    # TODO check that input fields are valid

    itinerary = userprofile.itinerary_set.create(name = itinerary_name, 
                         start_date = start, end_date = end)
    itinerary.location_set.create(name = location_name, start_time = start,
                         end_time = end)
    return HttpResponseRedirect(reverse('main.views.profile', args={}))
