#imports argv module
from sys import argv

#imports variables from script name and
#   specified filenames, pretyped in shell
script, filename = argv

#stores the file filename in a variable as file class
txt = open(filename)

#prints the file name
print "Here's your file %r:" % filename

#prints the file text
print txt.read()

#close the file (sequential read requires restart to read again)
txt.close

#asks for file name again
print "Type the filename again:"

#stores in a variable the name of the file as string
file_again = raw_input("> ")

#stores in a variable the file_again name as a file class
txt_again = open(file_again)

#prints the file text
print txt_again.read()

#close the file (sequential read requires restart to read again)
txt_again.close()
