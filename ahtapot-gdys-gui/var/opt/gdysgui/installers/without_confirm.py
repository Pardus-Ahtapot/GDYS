#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
from os import walk
from ConfigParser import ConfigParser
from datetime import datetime
import re
from time import sleep
import gitlab_check as GC
import config_parser as CP
import start_fw
import ahtapot_utils
from dmrlogger import Syslogger
from dmrlogger import Filelogger
import sys

abs_path = os.path.abspath(__file__)
path_list = abs_path.split("/")
del path_list[-1]
path_name = "/".join(path_list)
full_path = path_name + "/"

if os.path.exists(full_path + "current_user.dmr"):
    with open(full_path + "current_user.dmr") as current_user:
        user = current_user.readline()
else:
    user = subprocess.check_output(["whoami"])

filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",user)

def check_port(cmd_value, cmd_type):
    port_number = CP.get_configs()['port_number']
    if port_number != "" and port_number is not None:
        if cmd_type == "ssh":
            return cmd_value[:4] + "-p " + str(port_number) + " " + cmd_value[4:]
        elif cmd_type == "scp":
            return cmd_value[:4] + "-P " + str(port_number) + " " + cmd_value[4:]
        else:
            return None
    else:
        return cmd_value

def add_kerneltz(folder_path, file_name):

    try:
        cp_file = folder_path + file_name + ".tmp"
        org_file = folder_path + file_name
        p = subprocess.Popen(["grep","m time --kerneltz",org_file], stdout=subprocess.PIPE)
        out, err = p.communicate()
        if len(out) == 0:
            sed_cmd = "sed \"s/ -m time / -m time --kerneltz /g\" " + org_file + " > " + cp_file + " ; mv " + cp_file + \
                  " " + org_file
            subprocess.call([sed_cmd], shell=True)
    except Exception as e:
        filelogger.send_log("error"," while adding --kerneltz parameter : "+str(e))

def main():
    """
        Tests Firewall Builder Scripts on Test Machine. If there is no error,
        commits scripts to Gitlab.
    """

    #config for copying files
    fw_path = CP.get_configs()['fw_path']
    fw_copy_path = CP.get_configs()['fw_copy_path']
    copy_fws = fw_copy_path + "*.fw"
    rm_fws = fw_copy_path + "cp_*"
    poc_ip = CP.get_configs()['poc_ip']
    poc_user = CP.get_configs()['poc_user']
    poc_copy_location = CP.get_configs()['poc_copy_location']
    fwb_file = CP.get_configs()['fwb_file_name']
    std_out_err = CP.get_configs()['std_out_err']

    gitlab_user = CP.get_configs()['gitlab_user']
    gitlab_pass = CP.get_configs()['gitlab_pass']
    gitlab_url = CP.get_configs()['gitlab_url']
    gitlab_project_id = int(CP.get_configs()['gitlab_project_id'])

    master_branch = CP.get_configs()["gitlab_master_branch"]
    confirm_branch = CP.get_configs()["gitlab_confirm_branch"]



    scp_cmd = check_port("scp "+ rm_fws + " " + poc_user + "@" + poc_ip + ":" + poc_copy_location, "scp")
    rm_cmd = "rm -f " + rm_fws
    #ssh_rm_cmd = "ssh " + poc_user + "@" + poc_ip + " " + "\"rm -f "+poc_copy_location + "*.fw\""
    files = []
    for (dirpath, dirnames, file_names) in walk(fw_path):
        files.extend(file_names) #get filenames
        break
    file_list = [] #black and white list files
    for x in files:
        f_name, f_extension = os.path.splitext(x)
        if f_extension == ".fw":
            add_kerneltz(fw_path, x)
            path_write = fw_copy_path+"cp_"+x
            f_write = open(path_write,"w")
            with open(fw_path+x,'r') as f:
                lines = f.readlines()
            i = 1
            check_file=False
            #edit script for preventing "IP"(firewall IPs) errors and restore iptables on test machine
            for line in lines:
                if i == 2 :
                    f_write.write("sudo iptables-save > "+ poc_copy_location +"iptables.dmr\n")
                if re.search("configure_interfaces",line) and not re.search("{",line):
                    continue
                if re.search("verify_interfaces",line) and not re.search("{",line):
                    continue
                if re.search("prolog_commands",line) and not re.search("{",line):
                    continue
                if re.search("epilog_commands",line) and not re.search("{",line):
                    continue
                if re.search("esac",line):
                    f_write.write(line)
                    f_write.write("\nsudo iptables-restore < "+ poc_copy_location +"iptables.dmr\n")
                    f_write.write("rm -f "+ poc_copy_location +"iptables.dmr")
                    continue
                #check for necessary files on script if
                if re.search("check_file",line) and re.search("{",line):
                    check_file=True
                if check_file==True and re.search("exit",line):
                    f_write.write("\techo \"Can not find file $2\" 1>&2;\n")
                    f_write.write(line)
                    check_file=False
                    continue
                if re.search("check_file",line) and not re.search("{",line):
                    file_path = line.split(" \"")[2].split("\"")[0]
                    file_list.append(file_path) # add to file list
                f_write.write(line)
                i+=1
            f_write.close()
    if len(file_list) != 0:
        for f in file_list: # loop for every black/white list files
            dir_name = os.path.dirname(f)
            try:
                #preparing commands to be runned on test machine by checking if directory exists, if not create it.
                scp_cmd_file = check_port("scp " +f + " " + poc_user + "@" + poc_ip + ":" + dir_name, "scp")
                ssh_cmd_file = check_port("ssh " + poc_user+ "@" + poc_ip + " \"sudo /bin/bash -c 'if [ -d "+ dir_name +" ]; then echo 'hey'; fi'\"", "ssh")

                out = subprocess.check_output([ssh_cmd_file],shell=True)
                if out:
                    subprocess.call([scp_cmd_file],shell=True)
                else:
                    ssh_cmd = check_port("ssh "+ poc_user + "@" + poc_ip + " \"sudo /bin/bash -c 'mkdir -p "+ dir_name + "'\"", "ssh")
                    subprocess.call([ssh_cmd],shell=True)
                    subprocess.call([scp_cmd_file],shell=True) # copy black/white list files
            except Exception as exc_err:
                print "Gerekli Objeler Kopyalanirken hata olustu."
                filelogger.send_log("error"," address tables or objects couldn't be sent to test machine\n"+str(exc_err))
                print sys.exc_info()
                sleep(5)
                exit()
                #start_fw.kill_fw()
    try:
        #copy edited scripts to test machine to be runned
        subprocess.call([scp_cmd],shell=True)
        #remove copied scripts
        subprocess.call([rm_cmd],shell=True) #1
        filelogger.send_log("info"," changed firewall scripts were sent to test machine")
    except Exception as exc_err:
        print ".fw scriptleri kopyalanirken hata olustu."
        filelogger.send_log("error"," changed firewall scripts couldn't be sent to test machine\n"+str(exc_err))
        sleep(5)
        exit()
        #start_fw.kill_fw()

    files = []
    for (dirpath, dirnames, file_names) in walk(fw_path):
        files.extend(file_names) #get filenames
        break

    #command for deleting copied scripts on test machine for any conflict
    ssh_rm_script_cmd = check_port("ssh "+ poc_user + "@" + poc_ip + " \"rm -f " + poc_copy_location + "*\"", "ssh")
    #command for taking permission to run scripts
    ssh_chmod_cmd = check_port("ssh "+ poc_user + "@" + poc_ip + " \"chmod +x " + poc_copy_location + "*\"", "ssh")
    any_error = False
    error_out = ""
    error_script = ""
    #run every script on test machine and take errors and outputs
    for x in files:
        f_name, f_extension = os.path.splitext(x)
        if f_extension == ".fw":
            ssh_run_script_cmd = check_port("ssh "+ poc_user + "@" + poc_ip + " \"sudo /bin/bash -c " + poc_copy_location + "cp_" + x + "\"", "ssh")
            subprocess.call([ssh_chmod_cmd],shell=True)
            with open( std_out_err + "stdout","w") as fo: #<<<
                with open( std_out_err + "stderr","w") as fe:#<<<
                    p = subprocess.Popen(ssh_run_script_cmd,stdin=subprocess.PIPE,stdout=fo,stderr=fe,shell=True)
            sleep(3)
            with open( std_out_err + "stderr",'r') as f: #<<<
                error = f.readlines()
            if error:
                any_error = True
                error_script = x
                break
            break
    if any_error:
        print error
        print "Hata bulundu : ",error_script
        subprocess.call([ssh_rm_script_cmd],shell=True) #2
        filelogger.send_log("error"," error found on "+ str(error_script) + " : " + str(error))
        sleep(5)
        exit()
        #start_fw.kill_fw()
    else:
        filelogger.send_log("info"," scripts runned without error on test machine")

        git = GC.gitlab_connect(gitlab_url,gitlab_user,gitlab_pass)

        if GC.check_mergerequest(git,gitlab_project_id) == False:
            print u"Onay bekleyen bir yapilandirma mevcut\nLutfen daha sonra tekrar deneyiniz..."
            filelogger.send_log("error"," found a merge request while installing")
            sleep(5)
            exit()
            #start_fw.kill_fw()
        else:
            #check if git runs correctly
            if ahtapot_utils.check_git_status(fw_path)==False:
                print "Git ile ilgili bir hata mevcut, 'git status' komutuyla kontrol ediniz."
                filelogger.send_log("error"," there is an error about git path")
                sleep(5)
                exit()
                #start_fw.kill_fw()

            #create commits for every modified file and push
            if ahtapot_utils.check_git_status(fw_path) != True:
                date = datetime.strftime(datetime.now(),'%d/%m/%Y %H:%M:%S')
                ahtapot_utils.commit_files(fw_path,ahtapot_utils.get_changed_files(fw_path),date,confirm_branch)
                filelogger.send_log("info"," committed and pushed changes to repo")

                #Merge Request Comment and Createation
                merge_name = str(date) + " <-> " + unicode(user)
                cmd_checkout_master = "cd " + fw_path + " && git checkout "+master_branch
                cmd_pull_master = "cd " + fw_path + " && git pull"
                cmd_merge_master = "cd " + fw_path + " && git merge "+confirm_branch+" -m \"" + "merged from "+confirm_branch+" <-> " + unicode(user) + "\""
                cmd_push_merge = "cd " + fw_path + " && git push"
                cmd_checkout_confirm = "cd " + fw_path + " && git checkout "+confirm_branch

                subprocess.call([cmd_checkout_master],shell=True)
                subprocess.call([cmd_pull_master],shell=True)
                subprocess.call([cmd_merge_master],shell=True)
                subprocess.call([cmd_push_merge],shell=True)
                subprocess.call([cmd_checkout_confirm],shell=True)

                #rm scripts on test machine
                subprocess.call([ssh_rm_script_cmd],shell=True) #2
                filelogger.send_log("info"," created merge request")
                print u"Hatasiz Tamamlandi."
                print u"Firewall Builder 15 saniye sonra kapanacaktir..."
                sleep(15)
                filelogger.send_log("info"," killed Firewall Builder after install")
                start_fw.kill_fw()
            else:
                print u"Herhangi Bir Degisiklik Mevcut Degil."
                print u"Firewall Builder 15 saniye sonra kapanacaktir..."
                sleep(15)
                filelogger.send_log("warning"," No Change and killed Firewall Builder")
                start_fw.kill_fw()



if __name__=="__main__":
    main()
