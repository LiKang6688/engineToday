from django.conf.urls import patterns, include, url

urlpatterns = patterns('enginetoday.account.views',
    url(r'^$', 'settings', name='settings'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^emails/$', 'emails', name='emails'),
    url(r'^picture/$', 'picture', name='picture'),
    url(r'^password/$', 'password', name='password'),
)



