from __future__ import print_function
import os,random
import sys
import re
from termcolor import cprint

class errorcheck :

    def __init__(self) :
	pass		

	
    def decryption_error(self,output_file):
	self.outputfile=output_file

	fd=open(self.outputfile,'r')
	text_array=fd.readlines()
	fd.close()
	
        fd=open('/tmp/decrypt','r') 
	decrypt_text_array=fd.readlines()
	fd.close()

	if text_array == decrypt_text_array :
		return True

	else :
		return False

    def utf8_decoding(self):

	try:
    		with codecs.open('/tmp/1', 'w', decoding='utf8') as f:
        		decode_text=f.readlines()
    		f.close

	except Exception as e:
    		fatal = "excpetion caught while opening the file-%s" % e
    		cprint(fatal, 'red')


	try:
    		with codecs.open('/tmp/decrypt', 'w', decoding='utf8') as f:
        		decode_text_decrpyt=f.readlines()
    		f.close()

	except Exception as e:
    		fatal = "excpetion caught while opening the file-%s" % e
    		cprint(fatal, 'red')
    
    
    	if decode_text ==  decode_text_decrpyt :
        	return True 
    	else :
        	return False


    def rollback(self):
        pass


