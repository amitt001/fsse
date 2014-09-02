#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser
import argparse
import requests
import json


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("--type", dest="filetype", help="type of file too be searched")
    parser.add_argument("--startswith", dest="name", help="start or full name of file to be searched")
    args = parser.parse_args()

    path = '/home/amitt001/mycodes/dgplug/project/app/static/data.txt'
    fobj = open(path)
    raw_data = fobj.read()

    tags = json.loads(raw_data)
    obj = open('/tmp/search.txt', "w")
    for i in tags:
        if tags[i] == args.filetype: 
            s= str(i).split("/")[-1]
            if args.name in s:
                print(i)
                json.dump(i, obj)
                obj.write("\n")
    obj.close()
