from django.conf.urls.defaults import *

urlpatterns = patterns('flatpages_plus.views',
    # url(r'^(?P<url>.*)$',
    #     view='flatpage',
    #     name='flatpage'
    # ),
    (r'^list/', 'list'),
    (r'^add/', 'add'),
    (r'^update/(?P<id>\d+)/$', 'update'),
    (r'^delete/(?P<id>\d+)/$', 'delete'),
    (r'^confirm-delete/(?P<id>\d+)/$', 'confirm_delete'),
    (r'^search/$', 'search'),
    (r'^(?P<url>.*)$', 'flatpage'),
)
