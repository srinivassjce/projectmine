#!/usr/bin/python
import sys
import os
import re
import pdb
from termcolor import cprint
import glob
#importing libraries
from  lib.cryptomodule import *
from lib.rules import  *
from lib.errorhandling import *

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    #print directory
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == "__main__":
    cprint("Procesing the directory")

    for dir in os.listdir("../input/"):

        if dir == "FixedWidth" :
            dir_in="../input/FixedWidth/"
            for dir1 in os.listdir(dir_in) :
                #print dir1
                if dir1.lower() == "input".lower() :
                    dir_out="../input/FixedWidth/output/"
                    ensure_dir(dir_out)
                    r=rules_choice(dir_in)
                    r.zipfilehandling()



                    for name in glob.glob("../input/FixedWidth/input/*"):
                        if  os.path.isfile(name):
                            #procssing file
                            print fileoperations
                        else :
                            ensure_dir(name.replace('input','output'))
                            for  (_,_,files) in os.walk(name) :
                                if len(files) :
                                    for f in files :
                                     print   fileoperations


























