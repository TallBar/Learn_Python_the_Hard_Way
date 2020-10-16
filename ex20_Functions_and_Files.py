# Import argv from sys package
from sys import argv

# Set argv's
script, input_file = argv

# Define function that reads a file


def print_all(f):
    print f.read()

# Set the seek contents to the beginning


def rewind(f):
    f.seek(0)

# Function that print's an specific line in a file


def print_a_line(line_count, f):
    print line_count, f.readline()


# Define the file in project as the one from input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

# current_line = 2
current_line = current_line + 1
print_a_line(current_line, current_file)

# current_line = 3
current_line = current_line + 1
print_a_line(current_line, current_file)
