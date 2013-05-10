from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basePages.views.home', name='home'),
    url(r'^generallogin/$', 'basePages.views.generalLogin', name='login'),
    url(r'^generallogout/$', 'basePages.views.generalLogout', name='logout'),
    
    # url()
    url(r'^test/$', 'forum.views.PostComment', name='comment'),
    # url(r'^html5test/', include('html5test.foo.urls')),
    url(r'^time/$', 'timeview.views.index', name='timeview'),

    url(r'^space/$', 'space.views.index', name='spaceview'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))