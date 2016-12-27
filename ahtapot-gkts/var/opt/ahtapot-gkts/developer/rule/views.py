# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from rule.models import *

from datetime import datetime, timedelta
import sys
import os
import subprocess
import pytz

from dmr_utils.logger import get_logger

from django.utils import timezone


def home(request):

    return render(request, "home.html")


@login_required
def show_rules(request):

    rules = Rule.objects.filter(developer=request.user)

    activated_rules = ActivatedRule.objects.all()

    rule_list = []
    for a_rule in activated_rules:
        if Rule.objects.get(pk=a_rule.rule.id).developer == request.user:
            if a_rule.active_until > timezone.now():
                rule_list.append(a_rule.rule)

    return render(request, "show_rules.html", {'rules': rules, 'active_rules': rule_list})


@login_required
def show_activated(request):
    rules = ActivatedRule.objects.all()

    rule_list = []
    for a_rule in rules:
        if Rule.objects.get(pk=a_rule.rule.id).developer == request.user:
            rule_list.append(a_rule)

    return render(request, "show_activated.html", {'rules': rule_list, 'button': 'show'})


@login_required
def show_active(request):

    rules = ActivatedRule.objects.all()

    rule_list = []
    for a_rule in rules:
        if Rule.objects.get(pk=a_rule.rule.id).developer == request.user:
            if a_rule.active_until > timezone.now():
                rule_list.append(a_rule)

    return render(request, "show_activated.html", {'rules': rule_list, 'button': ''})


@login_required
def activate_rule(request):
    logger = get_logger()
    if request.POST:
        try:
            output_path = "../gkts"

            rule_id = request.POST["ruleId"]
            rule = Rule.objects.get(pk=int(rule_id))

            activated_rules = ActivatedRule.objects.filter(rule=rule)

            tz_current = timezone.now()
            for activated in activated_rules:
                if activated.rule.developer == request.user:
                    if activated.active_until > tz_current:
                        error_message = u"HATA: Bu Kural Zaten Şuan Aktif"
                        rules = Rule.objects.filter(developer=request.user)

                        return render(request, "show_rules.html", {'rules': rules, 'message': error_message})

            added_rule_time = datetime.now(pytz.timezone('UTC')) + timedelta(minutes=rule.time)
            r_time = datetime.strftime(added_rule_time, "%Y-%m-%dT%H:%M")
            rule_cmd = "{0} \"/sbin/iptables -I FORWARD 1 -p {4} --dport {3} -s {1} -d {2} -j ACCEPT -m time \
    --datestop {5}\"\n"

            format_rule_cmd = rule_cmd.format(rule.fqdn, rule.source, rule.destination,
                                              rule.destination_port, rule.protocol, r_time)

            with open(output_path, "a") as out_file:
                out_file.write(format_rule_cmd)
            # notifying ansible
            ansible_sh = '/var/opt/ahtapot-gkts/gktshook.sh'
            if os.path.exists(ansible_sh):
                try:
                    subprocess.call(["/bin/bash " + ansible_sh], shell=True)
                    logger.send_log("info", "Ansible Scripti calistirildi")
                except Exception as e:
                    logger.send_log("error","Ansible Scripti Calistirilamadi {}".format(str(e)))
            else:
                logger.send_log("error", "Ansible Scripti Bulunamadi")
            a_rule = ActivatedRule()
            a_rule.rule = rule
            a_rule.rule_cmd = format_rule_cmd
            a_rule.active_until = added_rule_time
            a_rule.save()

            logger.send_log("info", "Kural ID : " + str(rule.id) + " " + request.user.username + " aktif etti.")
            return HttpResponseRedirect("/rule/activated/")
        except Exception as e:
            error_message = "An error occured : {} ::: line : {}".format(str(e),sys.exc_info()[2].tb_lineno)
            logger.send_log("error", error_message)
            rules = {}
            return render(request,"show_activated.html",{'rules': rules, 'message': error_message})
