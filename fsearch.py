#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser
import argparse
import requests
import json


def fsearch(path, filetype, name):
    result = ""

    with open(path) as fobj:
        raw_data = fobj.read()

        tags = json.loads(raw_data)
#        obj = open('/tmp/search.txt', "w")
        for i in tags:

            if tags[i] == filetype: 

                s= str(i).split("/")[-1]

                if name in s:
                    result = result + i + " \n"
#                    json.dump(i, obj)
#                    obj.write("\n")
    return result


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("--type", dest="filetype", help="type of file too be searched")
    parser.add_argument("--init", dest="name", help="initials or full name of the file")
    args = parser.parse_args()

    with open(".config") as config:
        for loc in config:
            if "location" in loc:
                path = loc.split()[-1]

    print(fsearch(path, args.filetype, args.name))
