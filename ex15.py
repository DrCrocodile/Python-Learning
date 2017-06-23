# import the argument variables from system
from sys import argv
# assign those arguments to variable "script" and "filename"
script, filename = argv
# open that file and assign it to "txt"
txt = open(filename)
# print a sentence
print "Here's your file %r:" % filename
# read and print "txt"
#print txt.readline()
#print txt.tell()
#print txt.readline()
#print txt.tell()
#print txt.readline()
#print txt.tell()
print txt.read()
txt.close()
# print another sentence
print "Type the filename again:"
# assign your input to "file_again" with prompt "> "
file_again = raw_input("> ")
# open the file and assign it to "txt_again"
txt_again = open(file_again)
# read and print "txt_again"
print txt_again.read() 
txt_again.close()