from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

from bento.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name="homefood.html")),
    url(r'^items/',TemplateView.as_view(template_name="items.html")),
    url(r'^dallas/',TemplateView.as_view(template_name="dallas.html")),
    url(r'^home/',TemplateView.as_view(template_name="homefood.html")),

    url(r'^email_thali/','bento.views.send_email_thali',),   # to send emails from specific chef pages.
   
)
 