import string

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


fruit = 'Bananas'
fruit_copy = ''

for char in fruit:
   fruit_copy += char
   print(char, fruit_copy)


text = 'Hello, World!'
for index in range(len(text)):
    print(text[index])

    my_var = "42"

if type(my_var) == str:
    print("The value '{0}' is a string.".format(my_var))
else:
    print("The value {0} is NOT a string.".format(my_var))


title = 'The Hunger Games'
search_character = 'e'

if search_character in title:
   print("'{0}' is in '{1}'.".format(search_character, title))

# Make the check for vowels case-insensitive.
text = "Armadillos or anteaters"
vowels = 'aeiou'
vowel_count = 0

for char in text:
    if char.lower() in vowels:
        vowel_count += 1

print(f"'{text}' contains {vowel_count} vowels.")


# if char in '0123456789':
# if char in string.digits:
#
# # elif char in 'abcdefghijklmnopqrstuvwxyz':
# elif char in string.ascii_letters:
#
# else:

    # string.digits    Returns the string '0123456789'

    # string.ascii_lowercase   Returns the string 'abcdefghijklmnopqrstuvwxyz'

    # string.ascii_uppercase  Returns the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # string.ascii_letters Returns a string containing all of the uppercase and lowercase letters.

    # string.punctuation  Returns the string '!"#$%&'()*+,-./:;<= >?@[\]^_`{ |}~'.


print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


#
# if my_string in string.ascii_lowercase:
#     print("'{0}' is a lowercase letter.".format(my_string))
# elif my_string in string.ascii_uppercase:
#     print(f"{my_string} is an uppercase letter.")
# elif my_string in string.digits:
#     print(f"{my_string} is a digit")
# elif my_string in string.punctuation:
#     print(f"{my_string} is punctuation")
# else:
#     print(f"{my_string} is a something else")

my_string = '1fb\n#'
for char in my_string:

    if char in string.ascii_lowercase:
       print("'{0}' is a lowercase letter.".format(char))
    elif char in string.ascii_uppercase:
        print(f"{char} is an uppercase letter.")
    elif char in string.digits:
        print(f"{char} is a digit")
    elif char in string.punctuation:
        print(f"{char} is punctuation")
    elif char in string.whitespace:
        print(f"{char} is whitespace")
    else:
        print(f"{char} is somethign mysterious")





print('Characters'[8])
print("Strings are sequences of characters."[5])
print(len("Wonderful"))
print(len("Do spaces count?"))

# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

print(text[0:12])

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

print(text[-13:-1])

# 3. Print a slice of the middle 12 characters from 'text'.
start = int((len(text)/2) /2 -1 )
end = start + 12
print(text[start:end])

start = (len(text) - 12) // 2
print(text[start:start+12])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.

text = "word"

for char in reversed(text):
    print(char)

for char in text[::-1]:
    print(char)

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.


reversedWord = ""
for char in text[::-1]:
    reversedWord += char

print(reversedWord)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').

reversedWord = ""
for char in text[::-1]:
    reversedWord += char

print(f"{text} | {reversedWord}")


