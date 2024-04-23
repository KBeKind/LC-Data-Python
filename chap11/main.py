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






