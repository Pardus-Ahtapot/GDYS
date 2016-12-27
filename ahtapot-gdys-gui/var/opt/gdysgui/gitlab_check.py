#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gitlab
import os
import config_parser as CP
from datetime import datetime
import sys
from dmrlogger import Syslogger
from dmrlogger import Filelogger
from time import sleep
import subprocess


abs_path = os.path.abspath(__file__)
path_list = abs_path.split("/")
del path_list[-1]
path_name="/".join(path_list)
full_path = path_name + "/"

if os.path.exists(full_path + "current_user.dmr"):
    with open(full_path + "current_user.dmr") as current_user:
        user = current_user.readline()
else:
    user = subprocess.check_output(["whoami"])
logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", user)
filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a", user)

def gitlab_connect(gitlab_url,user,password):
    git = gitlab.Gitlab(gitlab_url)
    git.login(user=user,password=password)
    return git

def check_mergerequest(git,project_id):
    sleep(1)
    mergerequests = git.getmergerequests(project_id)
    if mergerequests != False:
        for merge in mergerequests:
            if merge["state"] == "opened" or merge["state"] == "reopened":
                return False
    return True

def create_mergerequest(git,project_id,source_branch,target_branch,title):
    return git.createmergerequest(project_id,source_branch,target_branch,title)

def get_mergerequest_status(git,project_id):
    if git.getmergerequests(project_id)!=False:
        if len(git.getmergerequests(project_id)) != 0:
            return git.getmergerequests(project_id)[0]["state"]
    return False

def check_merge_confirm():
    abs_path = os.path.abspath(__file__)
    path_list = abs_path.split("/")
    del path_list[-1]
    path_name = "/".join(path_list)
    full_path = path_name + "/"
    if os.path.exists(full_path + "onay.dmr"):
        return True
    return False

def get_projects(git):
    print git.getprojects()

def set_project_id(git,project_name):
    projects = git.getprojects()
    for project in projects:
        if project["name"] == project_name:
            CP.set_gitlab_config({"project_id":project["id"]})
def check_gitlab_connection(config):
    try:
        git = gitlab.Gitlab(str(config["gitlab_url"]))
        git.login(user=config["gitlab_user"],password=config["gitlab_pass"])
        return True,git
    except Exception as exc_err:
        logger.send_log("error", " Can't connect gitlab \n"+str(exc_err))
        filelogger.send_log("error", " Can't connect gitlab \n"+str(exc_err))
        return u"Gitlab bağlantı bilgileri hatalı.",False

def check_gitlab_settings(git,config):
    error_message = ""
    check_project = False
    project_id = ""
    for project in git.getprojects():
        if project["name"] == config["gitlab_project_name"]:
            check_project = True
            project_id = project["id"]
            break
    if check_project == False:
        return u" Proje Adı Hatalı "

    check_confirm_branch = False
    check_merge_branch = False
    for branch in git.getbranches(project_id):
        if branch["name"] == config["gitlab_confirm_branch"]:
            check_confirm_branch = True
        if branch["name"] == config["gitlab_master_branch"]:
            check_merge_branch = True
    if check_confirm_branch == False:
        return u" Onay Dalı Hatalı "
    if check_merge_branch == False:
        return u" Ana Dal Hatalı "

    return True

def return_date(dt):
    dt_list = dt.split(".")
    del dt_list[-1]
    dt = "".join(dt_list)
    dt = datetime.strptime(dt,"%Y-%m-%dT%H:%M:%S")

    new_date = dt.strftime("%d/%m/%Y %H:%M:%S")
    return new_date

def get_master_date(git,project_id,master_name):
    projects = git.getbranches(project_id)

    dt = ""

    for project in projects:
        if project["name"] == master_name:
            dt = project["commit"]["committed_date"]
    if dt!="":
        return return_date(dt)
    return False

def get_master_commit_id(git,project_id,master_name):
    projects = git.getbranches(project_id)
    if projects != False:
        for project in projects:
            if project["name"] == master_name:
                return str(project["commit"]["id"])
    return False


