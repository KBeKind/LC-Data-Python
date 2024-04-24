import random
import string

student = {
  'name' : 'Maria',
  'id_number' : 1234,
  'scores' : [90, 95, 88]
}

animal_info = {}

print(student)
print(student['name'])

print(animal_info)

print("*****************************")

favorite_ic_flavors = {
   'Mom' : 'vanilla',
   'Jerry' : 'Cherry Garcia',
   'Ben' : 'Chocolate Fudge Brownie',
   'Jenny' : 'Mint Chocolate Chip',
   'Odd choice' : 'pickled mango',
   'teachher' : 'Rocky Road'
}

print(favorite_ic_flavors)


favorite_ic_flavors["Mom"] = "chocolate chip"
favorite_ic_flavors["Klee"] = "reeses penut butter ice cream"
del(favorite_ic_flavors["Odd choice"])
favorite_ic_flavors["teacher"] = favorite_ic_flavors["teachher"]
del(favorite_ic_flavors["teachher"])

print(favorite_ic_flavors)

print("*****************************")


text = "What does the fox say?"
words = ['What', 'does', 'the', 'fox', 'say?']
state_capitals = {
   'MO' : 'Jefferson City',
   'CA' : 'Sacramento',
   'TX' : 'Austin',
   'HI' : 'Honolulu'
}

print(len(text))
print(len(words))
print(len(state_capitals))

print("*****************************")

num_animals = {
   'lions' : 3,
   'tigers' : 2,
   'bears' : 8,
   'pigeons' : 3000,
   'snakes' : 37,
   'Koalas' : 3
}

print(min(num_animals))
print(min(num_animals.items()))
print(max(num_animals.values()))

print("*****************************")

comics = {
   'Gary Larson' : 'The Far Side',
   'Terri Libenson' : 'Pajama Diaries',
   'Hilary B. Price' : 'Rhymes with Orange',
   'Jim Toomey' : "Sherman's Lagoon"
}

# Iterate by keys.
print("Here are the keys from the comics dictionary:")
for key in comics.keys():
   print(key)

# Iterate by values.
print("\nHere are the values from the comics dictionary:")
for value in comics.values():
   print(value)

# Access both keys and values.
print("\nHere are the key/value pairs from the comics dictionary:")
for key in comics.keys():
   print(f"Key: {key}, Value: {comics[key]}")

# Change the dictionary values.
print("\nUse a loop to change all of the values:")
for key in comics.keys():
   comics[key] = comics[key].upper()

print(comics)

print("*****************************")


comics = {
   'Gary Larson' : 'The Far Side',
   'Terri Libenson' : 'Pajama Diaries',
   'Hilary B. Price' : 'Rhymes with Orange',
   'Jim Toomey' : "Sherman's Lagoon"
}

# What gets printed if we don't attach .keys() or .values() to comics?
for data in comics:
   print(data)

print("*****************************")


comics = {
   'Gary Larson' : 'The Far Side',
   'Terri Libenson' : 'Pajama Diaries',
   'Hilary B. Price' : 'Rhymes with Orange',
   'Jim Toomey' : "Sherman's Lagoon"
}

# Iterate by keys, and print out the dictionary key/value pairs:
for key in comics.keys():
   print(key, comics[key])

# Iterate by key/value pairs:
for (key, value) in comics.items():
   print(key, value)

print("*****************************")

grocery_bill = {
   'bananas' : 1.77,
   'pears' : 6.97,
   'broccoli' : 1.98,
   'cheese' : 5.99,
   'soy milk' : 6.99,
   'orange juice' : 5.49,
   'eggs' : 1.98,
   'carrots' : 2.99
}
keys_list = list(grocery_bill.keys())
keys_list.sort()

for key in keys_list:
   print("{0}: {1}".format(key, grocery_bill[key]))

print("*****************************")

english_words = ['hello', 'your', 'there', 'stop', 'yes']
pirate_words = ['ahoy', 'yer', 'yonder', 'avast', 'aye']

# Create an empty 'translation' dictionary.
eng_to_pirate = {}

# We need to use index values to pull items from both lists.
for index in range(len(english_words)):
   eng_to_pirate[english_words[index]] = pirate_words[index]

print(eng_to_pirate)
print(eng_to_pirate['hello'].upper() + "!")

print("*****************************")

phone_book = {
   'Abby': '555-5081',
   'Mike': '555-5515',
   'Daniel': '555-5037',
   'Kimberly': '555-5509',
   'Jt': '555-5198',
   'Becky' : '555-5162',
   'Gordon' : '555-5299',
   'James' : '555-5837'
}
#
# name = input("Enter a name: ").lower().capitalize()
#
# if name in phone_book.keys():
#     print(f"The number for {name} is {phone_book[name]}.")
# else:
#     print(f"{name} is not in the phone book")
#     answer = input(f"Would you like to add {name} to the phone book? 'Y' or 'N'")
#     if answer.upper() == "Y":
#         new_phone_number = input(f"Please provide {name}'s phone number: ")
#         phone_book[name] = new_phone_number
#         print(f"{name} was added with the number: {new_phone_number}")
#     else:
#         print(f"We will not add {name} to the phone book.")
#
# ph_number = input("Enter a phone number: ")
# if ph_number not in phone_book.values():
#     print(f"{ph_number} is not in the phone book")
# else:
#     for (key, value) in phone_book.items():
#         if value == ph_number:
#             print(f"Dialing {ph_number} will call {key}.")
#
#

print("*****************************")



pass

# Write your fanciest_flavor function here:


def main():
  flavors = {
    'chocolate' : 0.35,
    'vanilla' : 0.35,
    'strawberry' : 0.42,
    'cookies and cream' : 0.45,
    'mint chocolate chip' : 0.42,
    'fudge chunk' : 0.45,
    'saffron' : 2.25,
    'garlic' : 0.05
  }

  choice = 'fudge chunk'
  price = return_cost(flavors, choice)
  if price == 0:
    print("Sorry, we don't have {0}.".format(choice))
  else:
    print(f"The price for {choice} is ${price} per scoop.")

  print('---')

  expensive_flavor = fanciest_flavor(flavors)

  print(f"The most expensive flavor we have is {expensive_flavor}.")

def return_cost(a_dictionary, flavor_choice):
    if flavor_choice in a_dictionary.keys():
        return a_dictionary[flavor_choice]
    else:
        return 0

def fanciest_flavor(a_dictionary):
    maximum_price = max(a_dictionary.values())
    for (key, value) in a_dictionary.items():
        if value == maximum_price:
            return key
    return 0

# main()

print("******************************")



# Code your assign_tickets function here:


# Code the fix_tickets function here:


def main():
    names = ['Caleb', 'Naomi', 'Owen', 'Ava', 'Aaron', 'Lydia']
    ticket_holders = assign_tickets(names)
    print(ticket_holders)
    fix_tickets(ticket_holders)

    return ticket_holders

def assign_tickets(names_list):
    names_dict = {}
    for a_name in names_list:
        names_dict[a_name] = random.randrange(100, 500)
    return names_dict

def fix_tickets(ticket_holders_dict):
    for (key, value) in ticket_holders_dict.items():
        if(value <= 199):
            ticket_holders_dict[key] = value + 500

# print(main())

print("***********************")

def main():
    text = "Python ROCKS!"
    results = character_count(text)
    print(f"The character counts for {text} is:")

    key_list = list(results.keys())
    key_list.sort()

    for (key) in key_list:
        if key in string.ascii_letters:
            print(f"{key}: {results[key]}")

def character_count(a_string):
    counts = {}
    for a_char in a_string:
        if a_char.upper() not in counts.keys():
            counts[a_char.upper()] = 1
        else:
            counts[a_char.upper()] += 1
    return counts

main()