# def remove_hyphens(str_with_hyphens):
#   without_hyphens = str_with_hyphens.replace('-', '')
#   phone_number = '1234'
#   print(phone_number)
#   return without_hyphens
#
# phone_number = "555-555-5555"
# no_hyph_number = remove_hyphens(phone_number)
# print(no_hyph_number)
# print(phone_number)
import string


# Part 1 A -- Make a Line

def make_line(size, icon = "#"):
  return(icon * size )


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square



print("**************************************")
# Part 1 C -- Make a Rectangle

def make_rectangle(width, height, icon = "#"):
  rectangle = ""
  for line in range(0, height):
    rectangle += make_line(width, icon)
    if line != height - 1:
      rectangle += "\n"
  return rectangle


print(make_rectangle(4,6))

print("**************************************")

def make_square(size, icon = "#"):
  return make_rectangle(size, size, "&")

print(make_square(4))

# Part 2 A -- Make a Stairs
print("************************")
def make_downward_stairs(height, icon = "#"):
  stairs = ""
  for line in range(0,height):
    stairs += make_line(line + 1, icon)
    if line != height - 1:
      stairs += "\n"
  return stairs

print(make_downward_stairs(4, "*"))
# Part 2 B -- Make Space-Line

def make_space_line(numSpaces, numChars, icon = "#"):
  return(f"{numSpaces * ' '}{numChars * icon}{numSpaces * ' '}")

print("***************************")
print(make_space_line(1,5, "%"))
# Part 2 C -- Make Isosceles Triangle
print("***************************")

def make_isosceles_triangle(height, icon = "#"):
  triangle = make_space_line(height - 1, 1, icon)
  triangle += "\n"
  for row in range(1,height):
    triangle += make_space_line(height - row - 1,  (row * 2) + 1, icon)
    if row != height - 1:
      triangle += "\n"
  return triangle

print(make_isosceles_triangle(4, "@"))
# Part 3 -- Make a Diamond
print("***************************")

def make_diamond(height, icon = "#"):
  top_half = make_isosceles_triangle(height, icon)
  bottom_half = top_half[::-1]
  diamond = top_half + "\n" + bottom_half
  return diamond

print(make_diamond(4, "$"))


print("***************************")
print("***************************")




# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# b) Within the function, use the 'list' function to split a string into a list of individual characters
# c) 'reverse' your new list.
# d) Use 'join' to create the reversed string and return that string from the function.
# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# g) Use method chaining to reduce the lines of code within the function.

def reverse_characters(aString):
  is_int = isinstance(aString, int)

  aString = str(aString)
  stringList = list(aString)
  stringList.reverse()
  aReversedString = "".join(stringList)

  if(is_int):
    return int(aReversedString)

  return aReversedString


print(reverse_characters("test"))

print(reverse_characters(1234) + 1)
# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.

def reverse_list(aList):
  aList.reverse()
  newList = []
  for item in aList:
    newList.append(reverse_characters(item))

  return newList



list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

print(reverse_list(list_test1))
print(reverse_list(list_test2))
print(reverse_list(list_test3))




# 4) Define a function with one parameter, which will be a string. The function must do the following:
# a) Have a clear, descriptive name.
# b) Retrieve only the last character from strings with lengths of 3 or less.
# c) Retrieve only the first 3 characters from strings with lengths larger than 3.
# d) Use a template literal to return the phrase, "We put the '___' in '___'." Fill the first blank with the modified string, and fill the second blank
# with the original string.

def put_the_in(aString):
  play_string = ""
  if len(aString) <= 3:
    play_string = aString[-1]
  else:
    play_string = aString[0:3]
  return f"We put the {play_string} in {aString}."

print(put_the_in("turtle"))

# Now test your function:
# e) Outside of the function, define the variable str and initialize it with a string (e.g. 'Functions rock!').


def area_of_rectangle(width, height):
  return width * height


print(area_of_rectangle(4,6))