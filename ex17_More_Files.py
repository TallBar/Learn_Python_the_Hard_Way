from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
# indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# all_in = open(from_file).read() + open(to_file, 'w').write(indata)

with open(from_file) as ff, open(to_file, 'w') as tf:
    content = ff.read()
    tf.write(content)
print "Alright, all done."

# out_file.close()
# # in_file.close()
# indata.close()

# No need to close because the context manager already does that
# ff.close()
# tf.close()
