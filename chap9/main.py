# Follow the instructions to see how the '+' and '*' operators affect lists.
import string

first_list = [3, 7, 5, 1, 7]
second_list = [6, 3, 9]

# Add your print statements here:

print(first_list + second_list)

print(second_list + first_list)

print(first_list * 3)

print(first_list)


fruit = ["apple", "orange", "banana", "cherry", "tomato", "bell pepper"]

print('apple' in fruit)       # 'apple' is an element in the list.
print('pear' in fruit)        # 'pear' is NOT in the list.
print('nana' in fruit)        # The string 'nana' is NOT an element in the list.
print('carrot' not in fruit)  # 'carrot' is missing from the list, so 'not in' returns True.

original_list = [2, 4, 6, 8, 10, 12, 14]

new_list = original_list[2:5]

print(new_list, 'vs.', original_list)
print(new_list[0])
print(original_list[:3])
print(original_list[3:])

print(12 in original_list[3:])


num_strings = ['one', 'two', 'three']
del num_strings[1]      # Removes the element at index 1.
print(num_strings)

letter_list = ['a', 'b', 'c', 'x', 'y', 'z']
del letter_list[1:5]    # Removes each element from index 1 - 4.
print(letter_list)



# Follow the listed steps (pun intended) to change one or more elements:
conjunctions = ['and', 'nor', 'yet', 'for', 'or', 'but', 'so']

print(conjunctions)
del conjunctions[1:2]
print(conjunctions)
del conjunctions[1:3]
print(conjunctions)
conjunctions[1:1] = ["test", "test2"]
print(conjunctions)
conjunctions[3:4] = ["replacing or"]
print(conjunctions)

shopping_list_items = ['apples', 'oranges', 'bananas', 'bread', 'toothpaste']

print('You need to buy:')
for item in shopping_list_items:     # Iterate by element
   print('\t' + item)

shopping_list_items = ['apples', 'oranges', 'bananas', 'bread', 'toothpaste']

for index in range(len(shopping_list_items)):  # Iterate by index
    print("{0}) {1}".format(index + 1, shopping_list_items[index]))


my_list = ['r', 'a', 't']

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)



evens = []     # evens is the accumulator variable

for num in range(0, 21, 2):  # num takes the values 0, 2, 4...20.
   evens.append(num)         # Add the value of num to the end of the list.

print(evens)



words = ['It', 'was', 'a', 'bright', 'cold', 'night', 'in', 'April', 'and', 'all', 'the', 'clocks', 'were', 'striking', 'thirteen']
a_words = []        # Accumulator list

for word in words:            # word takes the value of each element from words.
   if word[0].lower() == 'a': # True if word starts with 'a' or 'A'.
      a_words.append(word)    # Add word to the list.

print(a_words)



mixed_types = [5, 7, 3.14, 'rutabaga', 'integer', True]
integers = []
strings = []

for item in mixed_types:
   if type(item) == str:      # Check if item is a string data type.
      strings.append(item)
   elif type(item) == int:    # Check if item is an int data type.
      integers.append(item)

print(mixed_types)
print(integers)
print(strings)


strings = ['apple', 'banana', '1-to-1', '@launchcode', 'everyone can code', ':-)', '4EVR']
vowel_start = []
digit_start = []
other_start = []

# Add your loop here:

for aString in strings:
    if aString[0] in "aeiouAEIOU":
        vowel_start.append(aString)
    elif aString[0] in string.digits:
        digit_start.append(aString)
    else:
        other_start.append(aString)

print(vowel_start)
print(digit_start)
print(other_start)

numbers = [42, 27, 30, 46, -36, 30, -28, 53, 53, 32]
output = "Minimum = {0}, Maximum = {1}"

largest = max(numbers)
smallest = min(numbers)
print(numbers)
print(output.format(smallest, largest))


# Try to make list_a and list_b independent of each other.
list_a = [10, 33, 8, -2]
list_b = list_a.copy()
print(list_a, list_b)

list_b.sort()
list_a.append('hello')
print(list_a, list_b)



words = ['Hello', 'how', 'are', 'you?']
connector = '-'
new_string = connector.join(words)
print(words)

print('***'.join(words))
print('  '.join(words))


# Follow the given instructions to code a program that produces an alphebetized string.
tools = "hammer, screwdriver, pliers, drill, clamp"

tools_list = tools.split(", ")

print(tools_list)
tools_list.sort()
sorted_string = '*'.join(tools_list)

print(sorted_string)

print(tools)


text = 'Taco Cat'
other_text = 'Python ROCKS!'

# Reverse a string with a loop:
rev_text = ''
for char in text:
    rev_text = char + rev_text
    print(rev_text)

# Reverse a string with list & join:

char_list = list(other_text)
print(char_list)
char_list.reverse()
rev_other = ''.join(char_list)
print(rev_other)


two_dim_list = [['a', 'b', 'c'], [90, 101], [True, False, False, True]]

print(two_dim_list[0])     # Print the lists at indexes 0, 1, and 2
print(two_dim_list[1])
print(two_dim_list[2])

print(two_dim_list[0][2])  # Print the element from list 0, index 2
print(two_dim_list[1][1])  # Print the element from list 1, index 1
print(two_dim_list[2][3])  # Print the element from list 2, index 3




# Create the adding_practice list with the following entry: 273.15

adding_practice = [273.15]
print(adding_practice)

# Use the append method to add the number 42 and the string "hello" to the list. Add these new items one at a time.  Print the list after each step to confirm the changes.

adding_practice.append(42)
print(adding_practice)

adding_practice.append("hello")
print(adding_practice)

# Use list concatenation to add these three items to the list all at once: [False, -4.6, '87'].

adding_practice += [False, -4.6, "87"]
print(adding_practice)

# Use the cargo_hold list for the next set of exercises.
cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

# Use bracket notation to replace 'slinky' in the list with 'space tether'. Print the list to confirm the change.

cargo_hold[5] = "space tether"
print(cargo_hold)

# Remove the last item from the list with pop. Print the element removed and the updated list.

print(cargo_hold.pop())
print(cargo_hold)

# Remove the first item from the list with pop. Print the element removed and the updated list.
print(cargo_hold.pop(0))
print(cargo_hold)

# append and insert require arguments inside the (). Add the items 1138 and ‘20 meters’ to the the list - the number at the start and the string at the end. Print the updated list to confirm the changes.
cargo_hold.append("20 meters")
print(cargo_hold)
cargo_hold.insert(0,1138)
print(cargo_hold)

# Use the remove method to take the parrot out of cargo_hold, then print the updated list.

cargo_hold.remove("parrot")
print(cargo_hold)

# Use .format() to print the final list and its length. "The list ___ contains ___ items."

print("The list {0} contains {1} items.".format(cargo_hold, len(cargo_hold)))


# Use slices to make the following changes to the cargo_hold list. Be sure to print the list after each step to confirm your work.
cargo_hold = [1138, 'space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether', '20 meters']

# Insert the string 'keys' at index 3 without replacing any other entries.

cargo_hold[3:3] = ["keys"]
print(cargo_hold)

cargo_hold.insert(1, "keys")
print(cargo_hold)

# Remove 'instruction manual' from the list. (Hint: The index method is helpful to avoid manually counting an index).

cargo_hold.pop(cargo_hold.index("instruction manual"))
print(cargo_hold)

cargo_hold.append("instruction manual")
print(cargo_hold)

cargo_hold.remove("instruction manual")
print(cargo_hold)

# Replace the elements at indexes 2 - 4 with the items 'cat', 'book', and 'string cheese'.

cargo_hold[2:5] = ["cat", "book", "string cheese"]
print(cargo_hold)

# Some methods—like append and pop—alter the original list, while others do not. Use the lists supplies_1 and supplies_2 to see if taking a slice or using the ``reverse`` and ``sort`` methods changes the original list.
supplies_1 = ['duct tape', 'gum', 3.14, False, 6.022e23]
supplies_2 = ['orange drink', 'nerf toys', 'camera', '42', 'Rutabaga']

# Print a slice of the last 3 items from supplies_1. Does slice alter the original list? Verify this by printing supplies_1 after taking the slice.

print(supplies_1[-3:])
print(supplies_1)

# reverse the first list, sort the second, and then print both lists. What is the difference between the two methods? Do reverse or sort alter the original lists?

supplies_1.reverse()
supplies_2.sort()

print(supplies_1)
print(supplies_2)


phrase = 'In space, no one can hear you code.'
my_list = ['B', 'n', 'n', '5']
cargo_hold = "water,space suits,food,plasma sword,batteries"

# The split and list methods convert a string into a list, while the join method does the opposite.

# See what happens when you print phrase.split() vs. phrase.split('e') vs. list(phrase). What is the purpose of the argument inside the ()?

print(phrase.split())
print(phrase.split("e"))
print(list(phrase))

# See what happens when you print ''.join(my_list) vs. 'a'.join(my_list) vs. '_'.join(my_list). What is the purpose of the argument inside the ()?

print("".join(my_list))
print("a".join(my_list))
print("_".join(my_list))


# Split the cargo_hold string at each comma, alphabetize the list with sort, then combine the elements into a new string. Use a hyphen to join the elements together in the string.

cargo_hold = cargo_hold.split(",")
cargo_hold.sort()
cargo_hold = ", ".join(cargo_hold)
print(cargo_hold)

# Do split, list, or join change the original string/list?
# no


# Lists can hold different data types, even other lists! A multi-dimensional list is one with entries that are also lists.

# Define and assign the element_1, element_2, and element_26 lists as specified in the instructions.

element_1 = ["hydrogen", "H", 1.008]
element_2 = ["helium", "He", 4.003]
element_26 = ["iron", "Fe", 55.85]

# Use the append method to add each of the element lists to 'table'. Print table to see its structure.
table = []
table.append(element_1)
table.append(element_2)
table.append(element_26)

print(table)

# Use bracket notation to examine the difference between printing table[1] and table[1][1]. Describe the difference out loud. Go ahead, talk to your screen.

print(table[1])
print(table[1][1])

# Using bracket notation and the table list, print the mass from element_1, the name from element_2 and the symbol from element_26.

print(f"mass of element 1: {table[0][2]}, name of element 2: {table[1][0]}, symbol of element 26: {table[2][1]}")

# table is an example of a 2-dimensional list. The first “level” contains the element lists, and the second level holds the name/symbol/mass values. Experiment! Create a 3-dimensional list and print out one entry from each level in the list.

table.append(["list level 2",["list level 3", "another level 3"]])

print(table)
print(table[3][1][1])


my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

firstLetters = my_string[0:3]
a_new_string = my_string.replace(firstLetters,"",)
a_new_string += firstLetters.lower()
a_new_string = a_new_string.capitalize()
# Use a template literal to print the original and modified string in a descriptive phrase.
#
# print(f"the original string: {my_string}.  pig latin string: {a_new_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

num_of_letters = 0
need_input = True
# while(need_input):

    # num_of_letters = input("Give me a number of letters to be relocated:")
    # if int(num_of_letters) >= len(my_string):
    #     need_input = True
    #     print(f"that number is too large the word is {len(my_string)} characters long")
    # else:
    #     need_input = False


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

# my_string = "LaunchCode"
#
# firstLetters = my_string[0:int(num_of_letters)]
# a_new_string = my_string.replace(firstLetters,"",)
# a_new_string += firstLetters.lower()
# a_new_string = a_new_string.capitalize()
# print(f"the original string: {my_string}.  pig latin string: {a_new_string}")


proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
print("test")
print(strings)
for a_string in strings:
    if ", " in a_string:
        a_list = a_string.split(", ")
        a_list.reverse()
        a_string = ", ".join(a_list)
        print(a_string)

    elif "," in a_string:
        a_list = a_string.split(",")
        a_list.reverse()
        a_string = ",".join(a_list)
        print(a_string)

    elif " " in a_string:
        a_list = a_string.split(" ")
        a_list.reverse()
        a_string = " ".join(a_list)
        print(a_string)

    elif ";" in a_string:
        a_list = a_string.split(";")
        a_list.reverse()
        a_string = ";".join(a_list)
        print(a_string)
    else:
        print("String has none")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.


food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food_list = food.split(",")
equipment_list = equipment.split(",")
pets_list = pets.split(",")
sleep_aids_list = sleep_aids.split(",")

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]

print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

user_selection = input("Select your cargo hold 0-3:")
valid_selections = ["0", "1", "2", "3"]
# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
while user_selection not in valid_selections:
    print("invalid selection")
    user_selection = input("Select your cargo hold 0-3:")

print(cargo_hold[int(user_selection)])

user_item_selection = input("provide an item for me to check for:")

if user_item_selection in cargo_hold[int(user_selection)]:
    print(f"Cabinet {user_selection} DOES contain {user_item_selection}.")
else:
    print(f"Cabinet {user_selection} DOES NOT contain {user_item_selection}.")

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
