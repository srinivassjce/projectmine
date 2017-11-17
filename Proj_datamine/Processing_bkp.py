#!/usr/bin/python
import sys
import os
import re
import pdb
from termcolor import cprint
import glob
sys.path.append("../lib/")
#importing libraries
from lib.cryptomodule import *
from lib import rules
from lib.rules import  *
from lib.errorhandling import *
import threading


def replacenth(string, sub, wanted, n) :
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return  newString


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    #print directory
    print directory
    print os.path.exists(directory) 
    print "--end"		
    if not os.path.exists(directory):
        os.makedirs(directory)
	return True
	
    return None	

def fileoper(name):
			if  os.path.isfile(name):
			    file_name=name.split('/')[-1]	
                            f_in="input/FixedWidth/input/%s"%file_name
			    f_out="/tmp/%s"%file_name
			    cmd="cp %s %s"%(f_in,f_out)	
			    os.system(cmd)
			    print "name is %s"%file_name		
			    print ("f_in %s"%f_in)
			    print("f_out %s"%f_out)
			    #pdb.set_trace()		
			    f=f_out			
                            file_oper=rules(f)
                            if r.zipflag :
                                file_oper.zipoperations
                            if r.headerflag :
                                file_oper.headeradd()
                            if r.ctrlflag :
                                file_oper.remove_ctrl_characters()

                            #utf8 encoding
                            utf8_out=file_oper.utf8_encoding()

                            #AES encryption
                            c =crypto('1234567890123456')

                            encryptfile = c.encrypt(utf8_out)
			    cmd="sudo cp %s /tmp/%s"%(encryptfile,file_name)
			    print "COmmand %s"%cmd
			    #pdb.set_trace()		
			    os.system(cmd)
	
                            filemove="cp /tmp/%s %s"%(file_name,dir_out)

                            os.system(filemove)



if __name__ == "__main__":
    cprint("Procesing the directory")

    for dir in os.listdir("input/"):

        if dir == "FixedWidth" :
            dir_in="input/FixedWidth/"
            for dir1 in os.listdir(dir_in) :
                #print dir1
                if dir1.lower() == "input".lower() :
                    dir_out="input/FixedWidth/output/"
                    ensure_dir(dir_out)
                    r=rules_choice(dir1)
			
                    r.zipfilehandling()
                    r.classifier()
                    r.removectrlchar()
                    r.classifier()
                    r.headeradd()
                    r.delimiterhandling()
                    r.errorfilerequied()


                    for name in glob.glob("input/FixedWidth/input/*"):
                        if  os.path.isfile(name):
			    file_name=name.split('/')[-1]	
                            f_in="input/FixedWidth/input/%s"%file_name
			    f_out="/tmp/%s"%file_name
			    cmd="cp %s %s"%(f_in,f_out)	
			    os.system(cmd)
			    print "name is %s"%file_name		
			    print ("f_in %s"%f_in)
			    print("f_out %s"%f_out)
			    f=f_out			
                            file_oper=rules(f)
                            if r.zipflag :
                                file_oper.zipoperations
                            if r.headerflag :
                                file_oper.headeradd()
                            if r.ctrlflag :
                                file_oper.remove_ctrl_characters()

                            #utf8 encoding
                            utf8_out=file_oper.utf8_encoding()

                            #AES encryption
                            c =crypto('1234567890123456')

                            encryptfile = c.encrypt(utf8_out)
			    cmd="sudo cp %s /tmp/%s"%(encryptfile,file_name)
			    print "COmmand %s"%cmd
			    os.system(cmd)
	
                            filemove="cp /tmp/%s %s"%(file_name,dir_out)

                            os.system(filemove)


                        else :
			    print "name %s"%name
			    subdir=replacenth(name, 'input','output', 2)	

			    a=subdir + "/"+str(name.split('/')[-1] )
                            print ensure_dir(a)

                            for  (_,_,files) in os.walk(name) :
                                if len(files) > 0 :
                                    for f in files :
					print "files %s"%f
					f=name + "/" + f
                                     	fileoper(f,a)


























