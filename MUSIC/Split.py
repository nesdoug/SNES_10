#!/usr/bin/python3


# to split a binary file into 2 smaller ones
# (so I don't have to change my linker files)
# adding _1 and _2 to the file name
# for SNES SPC files > $8000
# if file is < $8000 bytes, will output a single zero in second file.
# input binary up to $10000 bytes


import sys
import os

filename = sys.argv[1]
extension = filename.split(".")[-1]
newname1 = filename[0:-4] + "_1." + extension
newname2 = filename[0:-4] + "_2." + extension

#print(filename)
#print(newname1)
#print(newname2)

oldfile = open(filename, 'rb')
newfile1 = open(newname1, 'wb')  # warning, this may overwrite old file !
newfile2 = open(newname2, 'wb')  # warning, this may overwrite old file !
filesize = os.path.getsize(filename)

#inarray[] = oldfile

if(filesize < 1) or (filesize > 0x10000):
    print("filesize error")
    exit()

if(filesize <= 0x8000):
    print("warning, filesize <= 0x8000. Didn't need to split.")
    for a in range (0,filesize):
        newfile1.write(oldfile.read(1))
    newfile2.write(bytes([0]))
    
else:
    for a in range (0,0x8000):
        newfile1.write(oldfile.read(1))
    filesize2 = filesize - 0x8000
    for a in range (0,filesize2):
        newfile2.write(oldfile.read(1))


print("done")


# close the files.
oldfile.close
newfile1.close
newfile2.close





