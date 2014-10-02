#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser
import json

tags = {"py":"python","txt":"text", "c":"c", "cpp":"c++", 
"swp": "swap", "pyc": "pycache", "zip":"zip", 
"rst":"ReStructuredText", "md": "markdown", 
"untagged": "unknown-Type", "jpg":"image", 
"png":"image", "jpeg":"image", "ko":"kernel", "o":"object", 
"flv":"video", "mkv":"video","mp4":"video"}


## checks known or unknown file?

def extension_check(extension):
    if tags.get(extension, 0) != 0:
        return 1
    else:
        return 0

####################################
##assign tags to the file and store 
####################################

indexed = {}

def assign(path, fname, tag):
    # to check if '/' is present as the last character
    slash = list(path)

    if(slash[-1] == "/"):
        path = path + fname
    else:
        path = path + "/" + fname

    indexed[path] = tags[tag]


#########################
####1,2,3-Start
#########################

if __name__ == "__main__":
    
    flag = 1
    counter = 0
    
    parser = ArgumentParser()
    parser.add_argument("-l", dest="location", default=os.getcwd(), help="Directory to be indexed")
    parser.add_argument("-s", dest="save", default="/tmp", help="Location of indexed file")
    args = parser.parse_args()
    
    path = args.location

    for names in os.walk(path):

        abs_path = names[0]

        for name in (names)[-1]:
            fname = name
            ext = name.split(".")[-1]
            flag = extension_check(ext)

            if flag == 0:
                ext = "untagged"

            assign(abs_path, fname, ext)    

    with open(".config") as config:
        for loc in config:
            if "location" in loc:
                save = loc.split()[-1]
    
#    if(args.save):
        os.chdir(args.save)
#    else:
#        os.chdir(save)

    with open("data.txt", "w") as output:
        json.dump(indexed, output)
