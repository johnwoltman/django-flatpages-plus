from django.conf.urls.defaults import *

urlpatterns = patterns('flatpages_plus.views',
    # url(r'^(?P<url>.*)$',
    #     view='flatpage',
    #     name='flatpage'
    # ),
    (r'^list/', 'list'),
    (r'^add/', 'add'),
    (r'^update/(?P<id>\d+)/$', 'update'),
    (r'^(?P<url>.*)$', 'flatpage'),
)
