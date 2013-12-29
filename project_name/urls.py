from django.conf.urls import patterns, include, url
import urls_examples
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^examples/',
                           include(urls_examples),
                           name='examples'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
