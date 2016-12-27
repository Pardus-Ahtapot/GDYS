#!/usr/bin/env python

import subprocess
import re
import os


def check_git_status(repo_path):
    status_cmd = "cd "+repo_path+ " && git status"
    p = subprocess.Popen([status_cmd],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()

    if out and not err:
        if re.search("nothing to commit",out):
            return True
    if err:
        return False
    return out
def check_and_print_error(out,err):
    if err:
        print "Hata : ", err
        print "Sonuc : ", out
        exit()

def get_changed_files(fw_path):

    git_status_cmd = "cd " + fw_path + " && git status"

    file_array = []

    p = subprocess.Popen(git_status_cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    out_lines = out.split("\n")
    for line in out_lines:
        if re.search("modified:",line):
            f_name, f_extension = os.path.splitext(line.split()[-1])
            if f_extension == ".fw":
                file_array.append(line.split()[-1])

    return file_array

def get_comments(file_path,file_name):
    path = file_path + file_name
    with open(path) as f:
        lines = f.readlines()
    comment_array = []
    i = 1
    for line in lines:
        if i >12:
            if str(line)[0] == "#":
                line = str(line.split("\n")[0])
                line = line[1:]
                comment_array.append(line)
            else:
                break
        i+=1
    return comment_array

def commit_files(fw_path,file_array,prefix_message,push_branch):
    for f in file_array:
        comments = get_comments(fw_path,f)
        comment = " ".join(comments)
        git_add_cmd = "cd " + fw_path + " && git add " + f
        git_commit_cmd = "cd " + fw_path + " && git commit -m \"" + prefix_message + " - " + f + " : " +comment + "\""
        p=subprocess.Popen([git_add_cmd],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out, err = p.communicate()
        check_and_print_error(out,err)
        p=subprocess.Popen([git_commit_cmd],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out, err = p.communicate()
        check_and_print_error(out,err)
    git_other_add_cmd = "cd " + fw_path + " && git add ."
    git_other_commit_cmd = "cd " + fw_path + " && git commit -m \""+ prefix_message +" : Detay Yok\""
    git_push_cmd = "cd " + fw_path + " && git push origin " + push_branch
    p=subprocess.Popen([git_other_add_cmd],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    check_and_print_error(out,err)
    p=subprocess.Popen([git_other_commit_cmd],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    check_and_print_error(out,err)
    p=subprocess.Popen([git_push_cmd],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()