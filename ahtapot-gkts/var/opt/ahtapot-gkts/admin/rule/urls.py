from django.conf.urls import url

from rule.views import *

urlpatterns = [
    url(r'^show/', show_rules, name='show_rules'),
    url(r'^activate/', activate_rule, name='activate_rules'),
    url(r'^activated/', show_activated, name='show_activated'),
    url(r'^active/', show_active, name='show_active'),
]
