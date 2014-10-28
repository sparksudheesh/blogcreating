from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = patterns('',
    url(r'^users/$', views.ProfileList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)