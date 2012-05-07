from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^itineroid/', include('itineroid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin pages
    (r'^admin/', include(admin.site.urls)),

    (r'^accounts/', include('userena.urls')),

    url(r'^$', 'main.views.home'),

    # Media Files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
      {'document_root' : settings.MEDIA_ROOT}),
)
