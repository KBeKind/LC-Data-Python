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