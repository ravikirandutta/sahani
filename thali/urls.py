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
    url(r'^biryani/',TemplateView.as_view(template_name="biryani.html")),
    url(r'^home/',TemplateView.as_view(template_name="homefood.html")),
    url(r'^register/',TemplateView.as_view(template_name="register.html")),
    url(r'^handlelogin/','bento.views.handle_login', name="handlelogin"),
    url(r'^email_thali/','bento.views.send_email_thali',),   # to send emails from specific chef pages.
    url(r'^list/$', 'bento.views.list', name='list'),

    #url(r'accounts/register/$', TakeAwayRegistrationView.as_view(),name = 'registration_register'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
)


