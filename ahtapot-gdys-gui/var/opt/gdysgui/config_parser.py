#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
import os
import base64


Config = ConfigParser()

abs_path = os.path.abspath(__file__)
path_list = abs_path.split("/")
del path_list[-1]
path_name = "/".join(path_list)
full_path = path_name + "/"

Config.read(full_path + "config.ini")
#reading from config sections
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("Gec  %s" % option)
        except:
            print("Hata : %s!" % option)
            dict1[option] = None
    return dict1


def get_configs():
    Config.read(full_path + "config.ini")
    config = {}
    #Path Configs
    config["fw_path"] = ConfigSectionMap("Paths")['fw_path']
    config["fw_copy_path"] = ConfigSectionMap("Paths")['fw_copy_path']
    config["copy_fws"] = config["fw_copy_path"] + "*.fw"
    config["rm_fws"] = config["fw_copy_path"] + "cp_*"
    config["poc_ip"] = ConfigSectionMap("Paths")['poc_ip']
    config["poc_user"] = ConfigSectionMap("Paths")['poc_user']
    config["poc_copy_location"] = ConfigSectionMap("Paths")['poc_copy_location']
    config["std_out_err"] = ConfigSectionMap("Paths")['std_out_err']
    config["fwb_file_name"] = ConfigSectionMap("Paths")['fwb_file_name']
    config["port_number"] = ConfigSectionMap("Paths")['port_number']

    #Gitlab Configs
    config["gitlab_url"] = ConfigSectionMap("GitLab")['url']
    try:
        config["gitlab_user"] = base64.b64decode(ConfigSectionMap("GitLab")['user'])
        config["gitlab_pass"] = base64.b64decode(ConfigSectionMap("GitLab")['pass'])
    except:
        config["gitlab_user"] = ""
        config["gitlab_pass"] = ""
    config["gitlab_confirm_branch"] = ConfigSectionMap("GitLab")['confirm_branch']
    config["gitlab_master_branch"] = ConfigSectionMap("GitLab")['master_branch']
    config["gitlab_project_name"] = ConfigSectionMap("GitLab")['project_name']
    config["gitlab_project_id"] = ConfigSectionMap("GitLab")['project_id']
    config["gitlab_confirmation"] = ConfigSectionMap("GitLab")['confirmation']


    return config

def get_path_configs():
    Config.read(full_path + "config.ini")
    config = {}
    #Path Configs
    config["fw_path"] = ConfigSectionMap("Paths")['fw_path']
    config["fw_copy_path"] = ConfigSectionMap("Paths")['fw_copy_path']
    config["copy_fws"] = config["fw_copy_path"] + "*.fw"
    config["rm_fws"] = config["fw_copy_path"] + "cp_*"
    config["poc_ip"] = ConfigSectionMap("Paths")['poc_ip']
    config["poc_user"] = ConfigSectionMap("Paths")['poc_user']
    config["poc_copy_location"] = ConfigSectionMap("Paths")['poc_copy_location']
    config["std_out_err"] = ConfigSectionMap("Paths")['std_out_err']
    config["fwb_file_name"] = ConfigSectionMap("Paths")['fwb_file_name']

    return config

def get_gitlab_configs():
    Config.read(full_path + "config.ini")
    config = {}
    #Gitlab Configs
    config["gitlab_url"] = ConfigSectionMap("GitLab")['url']
    try:
        config["gitlab_user"] = base64.b64decode(ConfigSectionMap("GitLab")['user'])
        config["gitlab_pass"] = base64.b64decode(ConfigSectionMap("GitLab")['pass'])
    except:
        config["gitlab_user"] = ""
        config["gitlab_pass"] = ""
    config["gitlab_confirm_branch"] = ConfigSectionMap("GitLab")['confirm_branch']
    config["gitlab_master_branch"] = ConfigSectionMap("GitLab")['master_branch']
    config["gitlab_project_id"] = ConfigSectionMap("GitLab")['project_id']
    config["gitlab_project_name"] = ConfigSectionMap("GitLab")['project_name']
    config["gitlab_confirmation"] = ConfigSectionMap("GitLab")['confirmation']

    return config

def get_gitlab_connection():
    Config.read(full_path + "config.ini")
    config = {}
    config["gitlab_url"] = ConfigSectionMap("GitLab")['url']
    try:
        config["gitlab_user"] = base64.b64decode(ConfigSectionMap("GitLab")['user'])
        config["gitlab_pass"] = base64.b64decode(ConfigSectionMap("GitLab")['pass'])
    except:
        config["gitlab_user"] = ""
        config["gitlab_pass"] = ""
    config["gitlab_project_name"] = ConfigSectionMap("GitLab")['project_name']
    return config

def config_write(): #to change config.ini with new settings
    with open(full_path + 'config.ini', 'wb') as configfile:
        Config.write(configfile)
    configfile.close()

def set_path_config(new_config):
    for key,value in new_config.iteritems():
        Config.set("Paths",key,value)
    config_write()
def set_gitlab_config(new_config):
    for key,value in new_config.iteritems():
        if key == "pass" or key=="user":
            value = base64.b64encode(str(value).encode("utf-8"))
        Config.set("GitLab",key,value)
    config_write()