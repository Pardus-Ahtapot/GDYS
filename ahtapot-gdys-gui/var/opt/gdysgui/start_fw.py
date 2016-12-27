#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
import sys
from time import sleep
from ConfigParser import ConfigParser
import subprocess
import re
import os
import config_parser as CP
import signal
import gitlab_check as GC
import shutil
from distutils.dir_util import copy_tree


def start_fwbuilder(git):

    fw_path = CP.get_configs()['fw_path']
    file_name = CP.get_configs()['fwb_file_name']
    run_fwb = fw_path + file_name

    if GC.check_mergerequest(git,CP.get_configs()["gitlab_project_id"]) == True:
        change_file_mod = "chmod 644 " + run_fwb
        subprocess.call([change_file_mod],shell=True)
    else:
        change_file_mod = "chmod 444 " + run_fwb
        subprocess.call([change_file_mod],shell=True)

    subprocess.Popen(["fwbuilder", "-f",run_fwb])

def start_fwbuilder_temp():
    fw_path = CP.get_configs()['fw_path']
    file_name = CP.get_configs()['fwb_file_name']
    project_name = CP.get_configs()['gitlab_project_name']
    master_branch = CP.get_configs()["gitlab_master_branch"]
    confirm_branch = CP.get_configs()["gitlab_confirm_branch"]
    run_fwb = "/tmp/" + project_name + "/" + file_name

    if os.path.exists("/tmp/"+str(project_name)):
        rm_cmd = "rm -rf /tmp/" + str(project_name)
        subprocess.call([rm_cmd],shell=True)

    copy_folder = "cp -avr "+fw_path+" /tmp/"
    subprocess.call([copy_folder],shell=True)

    cmd_git_undo = "cd /tmp/" + project_name + " && git checkout -- ."
    cmd_git_branch = "cd /tmp/" + project_name + " && git checkout "+master_branch
    cmd_git_pull = "cd /tmp/" + project_name + " && git pull --rebase origin "+master_branch
    subprocess.call([cmd_git_undo],shell=True)
    subprocess.call([cmd_git_branch],shell=True)
    subprocess.call([cmd_git_pull],shell=True)

    cmd_git_branch = "cd /tmp/" + project_name + "&& git checkout "+confirm_branch
    cmd_git_check_file = "cd /tmp/" + project_name + " && git checkout "+master_branch+" -- " + file_name
    subprocess.call([cmd_git_branch],shell=True)
    subprocess.call([cmd_git_check_file],shell=True)

    change_file_mod = "chmod 444 " + run_fwb
    subprocess.call([change_file_mod],shell=True)

    subprocess.Popen(["fwbuilder", "-f", run_fwb])



def check_if_runs():
    try:
        s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
        for x in s.stdout:
            res = re.search("fwbuilder",x)
            res2 = re.search("fwbuilder-ahtapot",x)
            if res is not None and res2 is None:
                return True
        return False
    except IOError:
        check_if_runs()

def check_config_paths(config):
    check_paths = True
    error_path = ""
    for key,value in config.iteritems():
        if key != "poc_user" and key!= "poc_ip" and key!= "copy_fws" and key!= "rm_fws":
            if key == "fwb_file_name":
                pass
            elif key == "poc_copy_location":
                pass
            else:
                if os.path.exists(value) == False:
                    check_paths = False
                    error_path = value
                    break
    if check_paths == False:
        return u"Hatalı Yapılandırma : " + error_path
    return check_paths


def kill_fw():
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    out, err = s.communicate()

    for line in out.splitlines():
            if "fwbuilder" in line and not "fwbuilder-ahtapot" in line:
                    pid = int(line.split(None,1)[1].split()[0])
                    os.kill(pid,signal.SIGKILL)

def kill_gui_user(username):
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    out, err = s.communicate()

    for line in out.splitlines():
            if "gdys-gui" in line and not username in line:
                    pid = int(line.split(None,1)[1].split()[0])
                    os.kill(pid,signal.SIGKILL)


def kill_gui():
    sleep(1)
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    out, err = s.communicate()

    for line in out.splitlines():
            if "gdys-gui" in line:
                    pid = int(line.split(None,1)[1].split()[0])
                    os.killpg(pid,signal.SIGKILL)
