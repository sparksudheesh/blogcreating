from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blogs.views import PostDetail, PostList

urlpatterns = patterns('',
    url(r'^$', PostList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', PostDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)