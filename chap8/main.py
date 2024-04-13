this_string = 'Zero-based indexing!'

print(this_string[3])

print('Alphabet soup'[-1])

# ---- Try It! ----

# Change the index values in lines 3 and 5 to see how they affect the output.


# Enter 40 into the brackets in line 3. What happens when you use an index value that is larger than the length of the string?


# Replace 40 inside the brackets with a negative number, like -1. What happens?


print(this_string[len(this_string)-1])


# Use the special characters for newline and tab to produce the indented, multi-line output shown in the instructions.

print('Use newline\n\tand tab\n\t\tcharacters to \n\t\t\tcreate this\n\t\toutput with\n\ta single\nprint statement.')


my_string = 'Hello'
my_number = 3
my_expression = my_string * my_number

output = '''This is my_string: "{}". 
This is a my_number: {}.
This is the length of my_string * my_number: {}
test'''


print(output.format(my_string, my_number, len(my_expression)))

# ---- Try It! ----
# Experiment with the format() string method.
# Run the program several times with different values for my_string and my_number.
# Change the order of my_number and my_string inside the format parentheses. What happens?
# Change the location of one set of {} in output. What happens?
# Remove one set of {} from output and run the program. What happens?
# Use four or more {} inside output and run the program. What happens?


# Refactor the string concatenation to use either .format() or an f-string instead.
plural_noun = 'turtles'
name = 'Klee'
verb = 'fly'
adjective = 'happy'
color = 'purple'

mad_lib = f"Python provides a {color} collection of tools — including {adjective} syntax and {plural_noun} — that allows {name} to {verb} with strings."

print(mad_lib)