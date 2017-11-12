#!/usr/bin/python
from __future__ import print_function
import os,random,fnmatch
import sys
import re
from termcolor import cprint
from zipfile import ZipFile as zip

class common:
	def __init__(self):
		pass

	def find_files(self,directory,pattern):
		for root, dirs, files in os.walk(directory):
			for basename in files:
				if fnmatch.fnmatch(basename, pattern):
					filename = os.path.join(root, basename)
					yield filename





class rules :

	def __init__(self,inputfolder) :
		self.inputfile=inputfolder


	def zipoperations(self):
		z = zip(zipName)
		for f in z.namelist():
			if f.endswith('/'):
				os.makedirs(f)
			else:
				z.extract(f)

	def headeradd(self):
		pass


	def delimiterhandling(self,presentdelimiter=None,expecteddelimiter=None):
		if presentdelimiter :
			pass


	def classifier(self):
		pass






class fileoperations:

	def __init__(self,filename):
		self.filename=filename

	def delimter_operations(self):
		pass

	def utf8_encoding(self):
		pass
	def header_add(self):
		pass

	def remove_ctrl_characters(self):
		fd = open (self.inputfile,'r') 
		lines=fd.read()
		#It will replace all ASCII control characters by an empty string.
		lines = re.sub(r'[\x00-\x1F]+', '',lines)
		fd.close()
	
		fd = open(self.inputfile,'w') 
		fd.write(lines)
		fd.close()



class rules_choice(rules):

	def __init__(self,folder):
		self.folder=folder

	def zipfilehandling(self):
		userchoice="zipfile handling required on folder-%s ? If YES Press [1] Else Press [0]"%self.folder
		cprint(userchoice,'blue')
		flag=raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)',flag)) :

			cprint ("user input is wrong ",'red',attrs=['bold'])
			cprint ("valid entry is 1 / 0",'green')
			flag = raw_input("INPUT : ")


		if flag == 1 :
			self.zipflag=True
			rules(self.folder).ziprequired()

		elif flag == 0  :
			self.zipflag = False

	def headeradd(self):
		userchoice="header handling required on folder-%s ? If YES Press [1] Else Press [0]"%self.folder
		cprint(userchoice,'blue')
		flag=raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)',flag)) :

			cprint ("user input is wrong ",'red',attrs=['bold'])
			cprint ("valid entry is 1 / 0",'green')
			flag = raw_input("INPUT : ")


		if flag == 1 :
			self.headerflag=True

		elif flag == 0  :
			self.headerflag=False


	def multithreading_required(self):
		userchoice = "Mult threading  handling required on folder-%s ? If YES Press [1] Else Press [0]" % self.folder
		cprint(userchoice, 'blue')
		flag = raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)', flag)):
			cprint("user input is wrong ", 'red', attrs=['bold'])
			cprint("valid entry is 1 / 0", 'green')
			flag = raw_input("INPUT : ")

		if flag == 1:
			self.threadingflag = True

		elif flag == 0:
			self.threadingflag = False


	def errorfilerequied(self):
		userchoice = "Error handling required on folder-%s ? If YES Press [1] Else Press [0]" % self.folder
		cprint(userchoice, 'blue')
		flag = raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)', flag)):
			cprint("user input is wrong ", 'red', attrs=['bold'])
			cprint("valid entry is 1 / 0", 'green')
			flag = raw_input("INPUT : ")

		if flag == 1:
			self.errorflag = True

		elif flag == 0:
			self.errorflag = False


	def removectrlchar(self):
		userchoice = "Remove character option is required on folder-%s ? If YES Press [1] Else Press [0]" % self.folder
		cprint(userchoice, 'blue')
		flag = raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)', flag)):
			cprint("user input is wrong ", 'red', attrs=['bold'])
			cprint("valid entry is 1 / 0", 'green')
			flag = raw_input("INPUT : ")

		if flag == 1:
			self.ctrlflag = True

		elif flag == 0:
			self.ctrlflag = False


if __name__ == "__main__" :
	#r=rules_choice('1')
	#r.zipfilehandling()
    c=common()

    for filename in c.find_files('/home/act/srinivas/Proj_datamine/input/FixedWidth/input', '*'):
        cprint (filename,'blue')


