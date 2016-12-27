#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Rule(models.Model):

    source = models.CharField(max_length=80, verbose_name="Kaynak", help_text="Kaynak IP veya FQDN Bilgisi Giriniz(Tek)")
    destination = models.CharField(max_length=80, verbose_name="Hedef", help_text="Hedef IP veya FQDN Bilgisi Giriniz(Tek)")
    destination_port = models.IntegerField(verbose_name="Hedef Port", help_text=u"Hedef Port Numarasını Giriniz(Tek)")
    protocol = models.CharField(max_length=80, verbose_name="Protokol", help_text=u"Protokol Bilgisini Giriniz(Tek)")
    time = models.IntegerField(verbose_name=u"Süre", help_text=u"Aktif Olacağı Süreyi Dakika Türünden Giriniz(Tek)")
    developer = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name=u"Geliştirici")
    fqdn = models.CharField(max_length=80, verbose_name=u"Güvenlik Duvarı", help_text=u"IP veya FQDN Giriniz(Tek)")
    definition = models.CharField(max_length=255, verbose_name=u"Açıklama", help_text=u"Maksimum 255 Karakter")

    def __str__(self):
        return self.fqdn + " |**| " + self.developer.username + " |**| " + self.source + " |**| " + self.destination +\
                " |**| " + str(self.destination_port)

    class Meta:

        verbose_name = "Kural"
        verbose_name_plural = "Kurallar"


class ActivatedRule(models.Model):

    rule = models.ForeignKey(Rule, verbose_name="Kural")
    rule_cmd = models.CharField(max_length=255, verbose_name="Kural Komutu")
    operated_at = models.DateTimeField(default=datetime.now(), verbose_name=u"Oluşturulma Tarihi")
    active_until = models.DateTimeField(default=datetime.now(), verbose_name=u"Aktif Kalacağı Zaman")

    def __str__(self):
        return self.rule

    class Meta:

        verbose_name = u"Aktif Edilmiş Kural"
        verbose_name_plural = u"Aktif Edilmiş Kurallar"


