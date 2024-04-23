import string
alphabet = string.ascii_uppercase
# The code below contains 3 syntax errors. Run the code as-is to generate the first error message.
# Use the message to find and fix the bug. Repeat for the other bugs.

# value = int(input("Enter an index value: "))
# index = value%26
#
# if value >= len(alphabet):
#   print("The letter at index {0} ({1}) is '{2}'.".format(value, index, alphabet[index]))
# else:
#   print("The letter at index {0} is '{1}'.".format(index, alphabet[index]))
#

# word = input("Enter a school-appropriate word: ")
# print("The last letter in '{0}' is '{1}'".format(word, word[len(word)-1]))
#
# first_num = int(input("Enter a whole number: "))
# second_num = int(input("Enter another whole number: "))
#
# print(f"For {first_num} and {second_num}:")
# print("\tSum = {0}".format(first_num + second_num))
# print("\tDifference = {0}".format(first_num - second_num))
# print("\tProduct = {0}".format(first_num * second_num))
# if second_num != 0:
#   print("\tQuotient = {0}".format(first_num / second_num))
# else:
#   print("\tQuotient = undefined (cannot divide by 0)")
#


# This program should convert points earned to a percent. Find and fix the logic errors.
points_earned = 23.4
points_possible = 25

percentage = points_earned/points_possible * 100
print(f"The student earned {points_earned} points out of {points_possible}, or {percentage}%.")

# Here are some test cases:
# Earning 8 out of 10 possible points = 80.0%.
# 11 of of 15 is 73.33333333333333%.
# 23.4 out of 25 93.6%.


# Fix the logic errors in the code to correctly report a student's letter grade!

output = "The student's score of {0}% is a(n) '{1}'."

score_percent = 93.5

if score_percent >= 90:
  letter_grade = 'A'
elif score_percent >= 80:
  letter_grade = 'B'
elif score_percent >= 70:
  letter_grade = 'C'
elif score_percent >= 60:
  letter_grade = 'D'
else:
  letter_grade = 'F'

print(output.format(score_percent, letter_grade))





username = 'Rsssa1'
is_valid = False
has_digit = False

# Add print statements as directed to help find and fix the logic error.

if len(username) >= 5 and len(username) <= 10:  # Check length.
  is_valid = True

  for char in username:  # Loop to check the characters in username.
    if char in string.digits:  # Check for a digit (0-9).
      has_digit = True
    elif char not in string.ascii_letters:  # Check for non-letters.
      is_valid = False


if is_valid and has_digit:
  print(f"'{username}' is a valid username.")
else:
  print((f"'{username}' is invalid."))