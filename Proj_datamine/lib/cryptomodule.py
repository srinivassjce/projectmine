#!/usr/bin/python
from __future__ import print_function
import os,random
import sys
import re


try :
    from Crypto.Cipher import AES
    from termcolor import cprint
    import  multiprocessing
    import threading
    import hashlib

except Exception as  e :

    print ("Could not able to import library-error : %s"%e)


class crypto :

    def __init__(self,key) :
        self.key=key
        if len(self.key) != 16 :
            cprint ("Fatal error :Encryption Key length is not 16 bytes !!!",'red')
            sys.exit(0)


    def encrypt(self,filename):
        chunksize=64*1024
        outputFile="/tmp/encrypt"
        filesize =str(os.path.getsize(filename)).zfill(16)
        IV=''
        for i in range(16) :
            IV += chr(random.randint(0,0xFF))
        encryptor = AES.new(self.key,AES.MODE_CBC,IV)
        with open(filename,'rb') as infile :
            with open(outputFile,'wb') as outputfile:
                outputfile.write(filesize)
                outputfile.write(IV)
                while True :
                    chunk=infile.read(chunksize)
                    if len(chunk) == 0 :
                        break;
                    elif len(chunk) % 16 != 0 :
                            chunk +=' ' * (16 - (len(chunk)%16))

                    outputfile.write(encryptor.encrypt(chunk))
        outputfile.close()
        infile.close()
        
        return outputFile

    def decrypt(self,filename):
        chunksize = 64 * 1024
        outputFile = "/tmp/decrypt"
        with open(filename, 'rb') as infile:
            filesize = long(infile.read(16))
            IV = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, IV)
            with open(outputFile, 'wb') as outputfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outputfile.write(decryptor.decrypt(chunk))
                outputfile.close
                infile.close


        return outputFile

#for doing unit testing
if __name__ == "__main__":
    c=crypto('1234567890123456')
    #file="/home/act/srinivas/Proj_datamine/input/FixedWidth/input/november-2/999999-96409-2017"
    #file = "/home/act/srinivas/Proj_datamine/input/fixed/SDN.XML"

#    encryptfile=c.encrypt(file)
    
#print (c.decrypt(encryptfile))
