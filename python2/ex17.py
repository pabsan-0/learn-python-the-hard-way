from sys import argv
import os

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# we could do these on one line too, how ?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()
# No need to close file like this because no Object of the class File was created


print "the input file is %d bytes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "a'ight, all done"

out_file.close()
# in_file.close()


# all this
# in a single line:     import os; os.system(cp sales.txt float.txt)
# also:                 import os; os.system("cp %s %s" % (from_file, to_file))
