# Method to store variables in script by getting feature argv from sys package
from sys import argv

# Set argv names
script, filename = argv

# Open file set in argv
txt = open(filename)

# Print the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# Request input filename
print "Type the filename again:"
file_again = raw_input("> ")

# Test, ex15_sample.txt = sample for user input
real_deal = "ex15_" + file_again + ".txt"

# Open file through input variable
txt_again = open(real_deal)

# Print open file contents
print txt_again.read()
