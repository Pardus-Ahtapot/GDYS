#!/usr/bin/python
import re
import sys
import os
master_fwb = False
fname="/etc/fw/editable_objects"
if not os.path.isfile(fname):
    sys.exit(0)
if os.stat(fname).st_size <= 1:
    master_fwb = True
with open(sys.argv[1]) as fwb:
    fwb_content = fwb.readlines()

with open(fname) as rw_objects:
    rw_object_list = rw_objects.readlines()

rw_object_set = set(map(str.strip, rw_object_list))
new_fwb = []

if sys.argv[2] == "revert":
    for line in fwb_content:
        match = re.search(r'\<Firewall.*name=\"(.*?)\".*',line)
        if match:
            line = line.replace("ro=\"True\"","ro=\"False\"")
        new_fwb.append(line)
    with open(sys.argv[1],'w') as new_fwb_f:
        for line in new_fwb:
            new_fwb_f.write("%s" % line)
    sys.exit(0)

for line in fwb_content:
    match = re.search(r'\<Firewall.*name=\"(.*?)\".*',line)
    if master_fwb:
        if match:
            line = line.replace("ro=\"True\"","ro=\"False\"")
    else:
        if match:
            name = match.group(1)
            if name not in rw_object_set:
                line = line.replace("ro=\"False\"","ro=\"True\"")
            else:
                line = line.replace("ro=\"True\"","ro=\"False\"")
    new_fwb.append(line)

with open(sys.argv[1],'w') as new_fwb_f:
    for line in new_fwb:
        new_fwb_f.write("%s" % line)

