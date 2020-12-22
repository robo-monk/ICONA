#!/usr/bin/env python3
import sys
import os

def read_svg(file):
    return open(file, "r").read()

def get_all_svg_from_dir(directory):
    dic = {}
    for file in os.listdir(directory):
        if file.endswith("svg"):
            f = os.path.join(directory, file)
            dic[file.split(".")[0]] = read_svg(f)
    return dic

if len(sys.argv) < 2:
    print("Please include the icons folder as an argument when your run ICONA")
else:
    directory = sys.argv[1]
    print(f"Creating a JSON file from dir [{directory}]")
    print(get_all_svg_from_dir(directory))
    
