#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from rule.models import *

from django.utils import timezone


class RuleAdmin(admin.ModelAdmin):
    list_display = ['fqdn', 'developer', 'source', 'destination', 'destination_port', 'definition', 'url']
    list_filter = ('id','fqdn', 'developer', 'source', 'destination', 'destination_port', 'definition')

    def url(self, obj):
        filter_url = "<a href='/admin/rule/activatedrule/?rule__id__exact={}'>Aktive Logları</a>".format(obj.id)
        return filter_url

    url.allow_tags = True
    url.short_description = u'Kuralı Filtrele'


class ActivatedRuleAdmin(admin.ModelAdmin):
    list_display = ['fqdn', 'developer', 'source', 'destination', 'destination_port', 'active_until', 'status']
    list_filter = ['rule', 'operated_at', 'active_until']

    def fqdn(self,obj):
        return obj.rule.fqdn

    fqdn.short_description = u'Güvenlik Duvarı'
    fqdn.admin_order_field = 'rule__fqdn'

    def developer(self,obj):
        return obj.rule.developer

    developer.short_description = u'Geliştirici'
    developer.admin_order_field = 'rule__developer'

    def source(self,obj):
        return obj.rule.source

    source.short_description = 'Kaynak'
    source.admin_order_field = 'rule__source'

    def destination(self,obj):
        return obj.rule.destination

    destination.short_description = 'Hedef'
    destination.admin_order_field = 'rule__destination'

    def destination_port(self,obj):
        return obj.rule.destination_port

    destination_port.short_description = 'Hedef Port'
    destination_port.admin_order_field = 'rule__destination_port'

    def status(self, obj):
        current_time = timezone.now()
        if current_time < obj.active_until:
            return "Aktif"
        else:
            return u"Aktif Değil"

    status.allow_tags = True
    status.short_description = u'Durum'

admin.site.register(Rule, RuleAdmin)
admin.site.register(ActivatedRule, ActivatedRuleAdmin)
