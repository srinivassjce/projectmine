# !/usr/bin/python
import sys
import os
import re
import pdb
from termcolor import cprint
import glob
sys.path.append("lib/")
import threading
try :
# importing libraries
	from lib.cryptomodule import *
	from lib import rules
	from lib.rules import *
	from lib.errorhandling import *

except Exception as e :
	fatal_msg="Exception caught while  importing the libraries-error %s"%e
	cprint (fatal_msg,'red')
	sys.exit(1)



#Function substitute nth string ==> used for input subdirectory matching
def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n - 1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString


#Function which create the output directory if not exists
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    # print directory
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True

    return None


#perform the fileoperation for input files based on rules
def fileoper(name, dir_out, r):
    if os.path.isfile(name):
        if name.split('/')[-2] == 'input':
            file_name = name.split('/')[-1]

        else:
            file_name = name.split('/')[-2] + '/' + name.split('/')[-1]

#	print "directory %s"%dir_out

        f_in = name

        f_out = "/tmp/%s" % name.split('/')[-1]
        cmd = "cp %s %s" % (f_in, f_out)
        os.system(cmd)

        f = f_out
        file_oper = rules(f)
        if r.zipflag:
            file_oper.zipoperations
        if r.headerflag:
            file_oper.headeradd()
        if r.ctrlflag:
            file_oper.remove_ctrl_characters()

        # utf8 encoding
        utf8_out = file_oper.utf8_encoding()

        # AES encryption
        c = crypto('1234567890123456')

        encryptfile = c.encrypt(utf8_out)
        cmd = "cp %s %s" % (encryptfile, f_out)
        os.system(cmd) 
	
	filemove = "cp %s %s" % (f_out, dir_out) 
        os.system(filemove) 


	'''
        if r.errorflag:
            try:
                decryptfile = decrypt(encryptfile)
                decrypt_flag = check_for_decryptionerror()
                decode_flag = check_for_decode_error(decryptfile)

            except Exception as  e:
                cprint ("Exception caught during decryption or decoding %s"%e)

	

	    if decrypt_flag  and decode_flag :

	        filemove = "cp %s %s" % (f_out, dir_out) 
		os.system(filemove) 
		#remove the orginal input file if file has no decode and decrypt errors
		#moving the input file (script will take care by  deleting it
		cmd="rm %s"%file_in
		#os.system(cmd)


	    else : 
		#mark as error_file and move based on error msg	
		pass

	    '''	


if __name__ == "__main__":
    cprint("Procesing the directory ",'green')
    main_input = raw_input("Enter the directory which you want to process options 1--> FixedWidth 2->Delimeter 3-->JSON 4-->XML : ")
    try:
        main_input = int(main_input)
    except Exception as e:
        msg = "Exception caught while giving the directory name-%s" % e
        cprint(msg, 'red')
        sys.exit(1)

    while not (main_input >= 1 and main_input <= 4):
        cprint("Wrong input", 'red')
        msg = "Valid inputs are 1 ,2 ,3,4 to speficy 1--> FixedWidth 2->Delimeter 3-->JSON 4-->XML"
        cprint(msg, 'blue')
        main_input = raw_input("enter the directory which you want to process : ")
        try:
            main_input = int(main_input)
        except Exception as e:
            msg = "Exception caught while giving the directory name-%s" % e
            cprint(msg, 'red')
            sys.exit(1)

   # for dir in os.listdir("input/"):
    dict_directory = {
                "FixedWidth": 1,
                "Delimited": 2,
                "JSON": 3,
                "XML": 4,
            }

    for (k, v) in dict_directory.items():
    	if v == main_input:
        	input_dir = k
		info="Selected set of Files to parsing => : %s "%k 
                
		cprint (info,'green', attrs=['bold'], end="\n")
 

    for dir in os.listdir("input/"):	
            if dir == input_dir:
                dir_in = "input/%s/" % input_dir
                for dir1 in os.listdir(dir_in):
		    #info="Input directory is %s"%dir1	
                    #cprint (info,'green')
                    if dir1.lower() == "input".lower():
			info="Input directory is %s"%dir1  
                        cprint (info,'green')
                        dir_out = "input/%s/output/"%input_dir
                        ensure_dir(dir_out)
                        r = rules_choice(dir1)
                        r.zipfilehandling()
                        r.classifier()
                        r.removectrlchar()
                        r.classifier()
                        r.headeradd()
                        r.delimiterhandling()
                        r.errorfilerequied()
                        d = dir_in + "/input/*"
                        for name in glob.glob(d):
                            if os.path.isfile(name):
                                fileoper(name, dir_out, r)
                            else:
                                subdir = replacenth(name, 'input', 'output', 2)
				
                                a = subdir + "/"
				ensure_dir(a)	
                                for (_, _, files) in os.walk(name):
                                    if len(files) > 0:
                                        for f in files:
                                            f = name + "/" + f
                                            fileoper(f, a, r)

