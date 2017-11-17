#!/usr/bin/python
from __future__ import print_function
import os,random,fnmatch
import sys
import re
from termcolor import cprint
from zipfile import ZipFile as zip
import codecs

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



	def __init__(self,file) :

		self.inputfile=file
		self.out = "/tmp/1"

	def zipoperations(self):
		z = zip.extractall(self.inputfile)
		print (z)

	def headeradd(self):
		pass


	def delimiterhandling(self,presentdelimiter=None,expecteddelimiter=None):
		if presentdelimiter :
			pass


	def classifier(self):
		pass

	def delimter_operations(self):
		pass

	def header_add(self):
		pass

	def remove_ctrl_characters(self):
		fd = open(self.inputfile, 'r')
		lines = fd.read()
		# It will replace all ASCII control characters by an empty string.
		lines = re.sub(r'[\x00-\x1F]+', '', lines)
		fd.close()

		fd = open(self.out, 'w')
		fd.write(lines)
		fd.close

	def utf8_encoding(self):
                print (self.out)
		try :
			fd1=open(self.out,'r')
			text=fd1.read()
			fd1.close
		except Exception as e :
			fatal="excpetion caught while opening the file-%s"%e
			cprint (fatal,'red')

		with codecs.open(self.out, 'w', encoding='utf8') as f:
			f.write(text)
			f.close
		return self.out


class rules_choice(rules):
	zipflag= False
	headerflag = False
	threadingflag=False
	errorflag=False
	ctrlflag=False

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
			zipflag=True
			rules(self.folder).ziprequired()

		elif flag == 0  :
			zipflag = False

	def headeradd(self):
		userchoice="header handling required on folder-%s ? If YES Press [1] Else Press [0]"%self.folder
		cprint(userchoice,'blue')
		flag=raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)',flag)) :

			cprint ("user input is wrong ",'red',attrs=['bold'])
			cprint ("valid entry is 1 / 0",'green')
			flag = raw_input("INPUT : ")


		if flag == 1 :
			headerflag=True

		elif flag == 0  :
			headerflag=False


	def multithreading_required(self):
		userchoice = "Mult threading  handling required on folder-%s ? If YES Press [1] Else Press [0]" % self.folder
		cprint(userchoice, 'blue')
		flag = raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)', flag)):
			cprint("user input is wrong ", 'red', attrs=['bold'])
			cprint("valid entry is 1 / 0", 'green')
			flag = raw_input("INPUT : ")

		if flag == 1:
			threadingflag = True

		elif flag == 0:
			threadingflag = False


	def errorfilerequied(self):
		userchoice = "Error handling required on folder-%s ? If YES Press [1] Else Press [0]" % self.folder
		cprint(userchoice, 'blue')
		flag = raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)', flag)):
			cprint("user input is wrong ", 'red', attrs=['bold'])
			cprint("valid entry is 1 / 0", 'green')
			flag = raw_input("INPUT : ")

		if flag == 1:
			errorflag = True

		elif flag == 0:
			errorflag = False


	def removectrlchar(self):
		userchoice = "Remove character option is required on folder-%s ? If YES Press [1] Else Press [0]" % self.folder
		cprint(userchoice, 'blue')
		flag = raw_input("INPUT : ")
		while not (re.match(r'(^0$|^1$)', flag)):
			cprint("user input is wrong ", 'red', attrs=['bold'])
			cprint("valid entry is 1 / 0", 'green')
			flag = raw_input("INPUT : ")

		if flag == 1:
			ctrlflag = True

		elif flag == 0:
			ctrlflag = False


if __name__ == "__main__" :
	r=rules_choice('/home/act/srinivas/Proj_datamine/input/FixedWidth/input/Novemver-2/')
	r.zipfilehandling()
	c=common()
	
	for filename in c.find_files('/home/act/srinivas/Proj_datamine/input/FixedWidth/input', '*'):
		cprint (filename,'blue')
		


