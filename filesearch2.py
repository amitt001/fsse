#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser
import json

tags = {"py":"python","txt":"text_file", 
"c":"c_program", "cpp":"c++_program", 
"swp": "swap_file", "pyc": "pycache_file", 
"zip":"zip_file", "rst":"restructured_text", 
"md": "markdown", "untagged": "unknown-Type"}

## To check if tags{} have the information about the tag
def extension_check(extension):
    if tags.get(extension, 0) != 0:
        return 1
    else:
        return 0

########################################################################
## assign tags to the file and store the complete path with tags in dict
########################################################################

indexed = {}

def assign(path, fname, tag):
    path = path + "/" +fname
    indexed[path] = tags[tag]

##########################
## it all starts here
#########################

if __name__ == "__main__":
    
    flag = 1
    counter = 0

    path = sys.argv[1]

    for names in os.walk(path):

        abs_path = names[0]

        for name in (names)[-1]:
            fname = name
            ext = name.split(".")[-1]
            flag = extension_check(ext)

            if flag == 0:
                ext = "untagged"

            assign(abs_path, fname, ext)    

    print("check")

    with open("data.txt", "w") as output:
        json.dump(indexed, output)
