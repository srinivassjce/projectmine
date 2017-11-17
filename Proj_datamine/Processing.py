#!/usr/bin/python
import sys
import os
import re
import pdb
from termcolor import cprint
import glob

sys.path.append("../lib/")
# importing libraries
from lib.cryptomodule import *
from lib import rules
from lib.rules import *
from lib.errorhandling import *
import threading


def replacenth(string, sub, wanted, n):
	where = [m.start() for m in re.finditer(sub, string)][n - 1]
	before = string[:where]
	after = string[where:]
	after = after.replace(sub, wanted, 1)
	newString = before + after
	return newString


def ensure_dir(file_path):
	directory = os.path.dirname(file_path)
	# print directory
	print
	directory
	print
	os.path.exists(directory)
	print
	"--end"
	if not os.path.exists(directory):
		os.makedirs(directory)
		return True

	return None


def fileoper(name,dir_out,r):
	if os.path.isfile(name):
		if name.split('/')[-2] == 'input' :
			file_name = name.split('/')[-1]

		else :
			file_name = name.split('/')[-2] + '/'+name.split('/')[-1] 


		f_in = "input/FixedWidth/input/%s"%file_name

		f_out = "/tmp/%s"%name.split('/')[-1]
		cmd = "cp %s %s"%(f_in,f_out)
		os.system(cmd)
		print ("name is %s"%file_name)
		print("f_in %s" % f_in)
		print("f_out %s" % f_out)
		# pdb.set_trace()
		f = f_out
		file_oper = rules(f)
		print ("class instance- %s"%r)
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
		print "directory name %ssand file %s dir_out %s"%(encryptfile,f_out,dir_out) 
		cmd = "cp %s %s" % (encryptfile, f_out)
		print "Command %s"%cmd
		# pdb.set_trace()
		os.system(cmd)
		
		filemove = "cp %s %s" % (f_out, dir_out)

		os.system(filemove)


if __name__ == "__main__":
	cprint("Procesing the directory ")
	main_input = raw_input(
		"enter the directory which you want to process options 1--> FixedWidth 2->Delimeter 3-->JSON 4-->XML : ")
	try:
		main_input = int(main_input)
	except Exception as e:
		msg = "Exception caught while giving the directory name-%s" % e
		cprint(msg, 'red')
		sys.exit(1)

while not (main_input >= 1 and  main_input <= 4):
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



for dir in os.listdir("input/"):
        dict_directory={
        "FixedWidth" : 1,
   	"Delimeter" : 2,
	"JSON" : 3,
	"XML" : 4,
	}

	for (k,v) in dict_directory.items():
	  if v == main_input : 
		input_dir=k


	if dir == input_dir:
		dir_in = "input/%s/"%input_dir
		for dir1 in os.listdir(dir_in):
			print "Input dir %s"%dir1
			if dir1.lower() == "input".lower():
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
				d=dir_in + "/input/*"
				for name in glob.glob(d):
					if os.path.isfile(name):
						fileoper(name, dir_out,r)
					else:
						print("name %s"%name)
						subdir = replacenth(name, 'input', 'output', 2)

						a = subdir + "/" 
						print ("sub directory is %s"%a)									
						for (_, _, files) in os.walk(name):
							if len(files) > 0:
								for f in files:
									print ("sub diectory files %s" %f)
									f = name + "/" + f
									fileoper(f, a,r)
