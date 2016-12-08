"""enginetoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('enginetoday',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('enginetoday.main.urls', namespace='main')),

    url(r'^signup/$', 'authentication.views.signup', name='signup'),
    url(r'^signin/$', 'authentication.views.signin', name='signin'),
    url(r'^signout/$', 'authentication.views.signout', name='signout'),
    url(r'^reset/$', 'authentication.views.reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'authentication.views.reset_confirm', name='password_reset_confirm'),
    url(r'^success/$', 'authentication.views.success', name='success'),

    url(r'^settings/', include('enginetoday.account.urls', namespace='settings')),


    url(r'^(?P<username>[^/]+)/$', 'advertise.views.advertises', name='advertises'),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
