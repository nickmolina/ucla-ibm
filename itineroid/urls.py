
from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from userena import views as userena_views

urlpatterns = patterns('',
    # Example:
    # (r'^itineroid/', include('itineroid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin pages
    (r'^admin/', include(admin.site.urls)),

    # url(r'^accounts/(\w+)/$', userena_views.profile_detail, 
    #  {'template_name': 'profile.html'}),
    url(r'^accounts/', include('userena.urls')),

    url(r'^$', 'main.views.home'),
    url(r'^profile/$', 'main.views.profile'),
    url(r'^profile/itinerary/$', 'main.views.itinerary'),
    url(r'^profile/itinerary/add/$', 'main.views.itineraryadd'),


    # Media Files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root' : settings.MEDIA_ROOT}),
)
